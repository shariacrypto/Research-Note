"""Utilitas bersama: HTTP dengan retry, .env, log kegagalan, snapshot CSV."""
from __future__ import annotations
import csv, json, os, time, datetime as dt
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "shariacrypto-research/1.0 (+https://shariacrypto.id)"}


def load_env(path: Path = ROOT / ".env") -> None:
    """Muat KEY=VALUE dari .env ke os.environ (tanpa menimpa yang sudah ada)."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def now_wib() -> str:
    return (dt.datetime.utcnow() + dt.timedelta(hours=7)).strftime("%Y-%m-%d %H.%M WIB")


class Fetcher:
    """Pembungkus requests: retry + backoff, cache per-run, catatan sukses/gagal."""

    def __init__(self, outdir: Path, retries: int = 3, timeout: int = 30):
        self.outdir = outdir
        self.retries, self.timeout = retries, timeout
        self.log: list[dict] = []
        self.cache: dict[str, object] = {}
        (outdir / "raw").mkdir(parents=True, exist_ok=True)

    def get(self, url: str, params: dict | None = None, headers: dict | None = None,
            name: str | None = None, optional: bool = False):
        key = url + json.dumps(params or {}, sort_keys=True)
        if key in self.cache:
            return self.cache[key]
        h = dict(UA, **(headers or {}))
        last = ""
        for i in range(self.retries):
            try:
                r = requests.get(url, params=params, headers=h, timeout=self.timeout)
                if r.status_code == 429:  # rate limit: tunggu lebih lama
                    last = "429 rate limit"
                    time.sleep(10 * (i + 1))
                    continue
                if r.status_code >= 400:
                    last = f"HTTP {r.status_code}: {r.text[:160]}"
                    if r.status_code in (401, 403, 404, 451):
                        break  # tidak akan berubah dengan retry
                    time.sleep(2 ** i)
                    continue
                data = r.json()
                self.cache[key] = data
                if name:
                    (self.outdir / "raw" / f"{name}.json").write_text(
                        json.dumps(data, ensure_ascii=False)[:5_000_000], encoding="utf-8")
                self.log.append({"ok": True, "name": name or url, "url": r.url})
                return data
            except (requests.RequestException, ValueError) as e:
                last = f"{type(e).__name__}: {e}"[:200]
                time.sleep(2 ** i)
        self.log.append({"ok": False, "name": name or url, "url": url,
                         "error": last, "optional": optional})
        return None

    def write_log(self) -> Path:
        p = self.outdir / "fetch_log.txt"
        lines = [f"# fetch log {now_wib()}"]
        for e in self.log:
            if e["ok"]:
                lines.append(f"OK    {e['name']}")
            else:
                tag = "SKIP " if e.get("optional") else "GAGAL"
                lines.append(f"{tag} {e['name']} — {e['error']} — {e['url']}")
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return p


class Snapshot:
    """Baris snapshot PANDUAN §8.1: metrik,nilai,satuan,sumber,waktu_data."""

    def __init__(self):
        self.rows: list[list] = []
        self.values: dict[str, float | str] = {}

    def add(self, metrik: str, nilai, satuan: str, sumber: str, waktu: str):
        if nilai is None:
            return
        if isinstance(nilai, float):
            nilai = round(nilai, 6 if abs(nilai) < 10 else 2)
        self.rows.append([metrik, nilai, satuan, sumber, waktu])
        self.values[metrik] = nilai

    def write(self, path: Path):
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["metrik", "nilai", "satuan", "sumber", "waktu_data"])
            w.writerows(self.rows)


def write_series(outdir: Path, name: str, rows: list[tuple], header: tuple):
    """Deret waktu untuk grafik: data/out/<run>/series/<name>.csv"""
    d = outdir / "series"
    d.mkdir(exist_ok=True)
    with (d / f"{name}.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def ts_date(t: float) -> str:
    if t > 1e11:  # milidetik
        t /= 1000
    return dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
