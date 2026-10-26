"""Render semua grafik dari satu spec JSON.
    python -m charts.render charts_APT.json [outdir]
Spec: {"defaults": {...}, "charts": [{"type": "fan", "out": "c_kipas.png", ...}, ...]}
Mencetak ukuran tiap PNG; gagal bila ada yang > 100 KB atau judul/sumber kosong."""
from __future__ import annotations
import json, sys
from pathlib import Path
from .lib import TYPES


def main(spec_path, outdir=None):
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    outdir = Path(outdir or Path(spec_path).parent)
    outdir.mkdir(parents=True, exist_ok=True)
    bad = 0
    for c in spec["charts"]:
        c = {**spec.get("defaults", {}), **c}
        for k in ("title", "src", "out"):
            if not c.get(k):
                print(f"  GAGAL {c.get('out', '?')}: kunci '{k}' wajib")
                bad += 1
        if not c.get("title") or not c.get("out"):
            continue
        c["out"] = str(outdir / c["out"])
        p = TYPES[c["type"]](c)
        kb = p.stat().st_size / 1024
        flag = "OK " if kb <= 100 else "BESAR"
        bad += kb > 100
        print(f"  {flag} {p.name}  {kb:.0f} KB  [{c['type']}] {c['title']}")
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(*sys.argv[1:3]) else 0)
