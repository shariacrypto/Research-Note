"""Uji otomatis PANDUAN v3.2: identitas suplai, rekonsiliasi konflik, beta, metrik turunan."""
from __future__ import annotations
import math, statistics as st, datetime as dt


def pct_diff(a, b):
    if a in (None, 0) or b is None:
        return None
    return abs(a - b) / abs(a) * 100


# ---------- konflik antar sumber ----------
def conflicts(pairs: list[tuple[str, float, str, float, str]], supply_tol=3.0, other_tol=20.0):
    """pairs: (metrik, nilai_a, sumber_a, nilai_b, sumber_b).
    Suplai: >3% = REKONSILIASI (PANDUAN §9.2). Lainnya: >20% = REKONSILIASI WAJIB (v3.2 §4A)."""
    out = []
    for m, a, sa, b, sb in pairs:
        d = pct_diff(a, b)
        if d is None:
            continue
        tol = supply_tol if "suplai" in m else (50.0 if "volume" in m else other_tol)
        # volume antar agregator memang sering beda 20–40% (cakupan bursa berbeda): ambang 50%
        if d > tol:
            out.append({"metrik": m, "a": a, "sumber_a": sa, "b": b, "sumber_b": sb,
                        "selisih_pct": round(d, 1),
                        "tindakan": "REKONSILIASI: cari sumber primer (explorer/dokumen resmi), "
                                    "jelaskan penyebab selisih; JANGAN memilih angka konservatif begitu saja"})
    return out


# ---------- identitas suplai ----------
def supply_identity(circ, total, maxs, components: dict[str, list]):
    """Uji: total − beredar = Σ komponen tidak beredar (±2% total); beredar ≤ total ≤ maks;
    komponen tidak boleh tumpang-tindih (cek manual: tandai komponen 'bagian_dari').
    components: {"nama": [jumlah, "sumber", opsional "bagian_dari"]}"""
    res = {"lulus": True, "temuan": []}
    if not circ or not total:
        res["lulus"] = False
        res["temuan"].append("Suplai beredar/total tidak tersedia: uji tidak bisa dijalankan")
        return res
    if circ > total * 1.001:
        res["lulus"] = False
        res["temuan"].append(f"Beredar ({circ:,.0f}) > total ({total:,.0f})")
    if maxs and total > maxs * 1.001:
        res["lulus"] = False
        res["temuan"].append(f"Total ({total:,.0f}) > maks ({maxs:,.0f})")
    gap = total - circ
    top = {k: v for k, v in components.items() if not (len(v) > 2 and v[2])}
    nested = {k: v for k, v in components.items() if len(v) > 2 and v[2]}
    s = sum(v[0] for v in top.values())
    resid = gap - s
    res.update({"tidak_beredar": gap, "jumlah_komponen": s, "sisa": resid,
                "sisa_pct_total": round(resid / total * 100, 2)})
    if components and abs(resid) > 0.02 * total:
        res["lulus"] = False
        res["temuan"].append(
            f"Selisih identitas {resid:,.0f} ({resid / total * 100:.1f}% total): komponen kurang, "
            "tumpang-tindih, atau sumber suplai beredar berbeda definisi")
    for k, v in nested.items():
        parent = components.get(v[2])
        if parent and v[0] > parent[0]:
            res["lulus"] = False
            res["temuan"].append(f"Komponen '{k}' ({v[0]:,.0f}) lebih besar dari induknya '{v[2]}'")
        res["temuan"].append(
            f"Catatan: '{k}' adalah BAGIAN dari '{v[2]}', tidak dijumlah dua kali (pelajaran APT 22 Okt 2026)")
    if not components:
        res["temuan"].append("Komponen tidak beredar belum diisi di config (suplai_manual.komponen)")
    return res


# ---------- deret harga → mingguan, beta ----------
def to_weekly(daily: list[tuple[str, float]]):
    """Ambil tiap hari ke-7 dari tanggal terakhir mundur (penutupan mingguan sederhana)."""
    pts = daily[::-1][::7][::-1]
    return pts


def align(a, b):
    db = dict(b)
    return [(d, x, db[d]) for d, x in a if d in db]


def beta(asset_weekly, btc_weekly, weeks=52):
    rows = align(asset_weekly, btc_weekly)[-(weeks + 1):]
    if len(rows) < 27:
        return None
    ra = [math.log(rows[i][1] / rows[i - 1][1]) for i in range(1, len(rows))]
    rb = [math.log(rows[i][2] / rows[i - 1][2]) for i in range(1, len(rows))]
    ma, mb = st.fmean(ra), st.fmean(rb)
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb)) / (len(ra) - 1)
    vb = st.variance(rb)
    corr = cov / (st.stdev(ra) * st.stdev(rb))
    return {"beta": round(cov / vb, 2), "korelasi": round(corr, 2), "n_minggu": len(ra),
            "vol_tahunan_pct": round(st.stdev(ra) * math.sqrt(52) * 100, 1),
            "return_asset_pct": round((rows[-1][1] / rows[0][1] - 1) * 100, 1),
            "return_btc_pct": round((rows[-1][2] / rows[0][2] - 1) * 100, 1),
            "dari": rows[0][0], "sampai": rows[-1][0]}


# ---------- metrik turunan untuk rubrik ----------
def window_sum(series, days, end_offset=0):
    s = [v for _, v in series if v is not None]
    if len(s) < days + end_offset:
        return None
    seg = s[len(s) - end_offset - days: len(s) - end_offset]
    return sum(seg)


def revenue_trend(series):
    """Rubrik J 'Tren pendapatan': kuartal terakhir ×4 vs 12 bln sebelum kuartal itu."""
    q = window_sum(series, 91)
    prev = window_sum(series, 365, end_offset=91)
    if q is None or not prev:
        return None
    return {"kuartal_x4": q * 365 / 91, "12bln_sebelumnya": prev,
            "perubahan_pct": round((q * 365 / 91 / prev - 1) * 100, 1)}


def change_12m(series):
    """Perubahan rata-rata 30 hari terakhir vs 30 hari setahun lalu (metrik penggunaan)."""
    s = [v for _, v in series if v is not None]
    if len(s) < 395:
        return None
    now, then = st.fmean(s[-30:]), st.fmean(s[-395:-365])
    return round((now / then - 1) * 100, 1) if then else None


def monthly_cv(series, months=12):
    """Rubrik N 'Stabilitas pendapatan': koefisien variasi pendapatan bulanan."""
    by = {}
    for d, v in series:
        if v is not None:
            by.setdefault(d[:7], 0)
            by[d[:7]] += v
    keys = sorted(by)[:-1][-months:]  # buang bulan berjalan yang belum penuh
    vals = [by[k] for k in keys]
    if len(vals) < 6 or st.fmean(vals) == 0:
        return None
    return {"cv": round(st.stdev(vals) / st.fmean(vals), 2), "bulan": keys,
            "nilai": [round(v) for v in vals]}


def app_fee_shares(protocols, cat_map: dict[str, str], override: dict[str, str]):
    """Porsi fee 30 hari per aplikasi di rantai → masukan L3/L4 syariah (v3.2 §4D).
    cat_map: kategori DefiLlama → halal|nonhalal|tinjau. override: slug → kelas."""
    tot = sum(p["d30"] or 0 for p in protocols)
    rows, agg = [], {"halal": 0, "nonhalal": 0, "tinjau": 0}
    for p in protocols:
        v = p["d30"] or 0
        if v <= 0:
            continue
        k = override.get(p.get("slug") or "", cat_map.get(p.get("category") or "", "tinjau"))
        agg[k] = agg.get(k, 0) + v
        rows.append({**p, "kelas": k, "porsi_pct": round(v / tot * 100, 2) if tot else None})
    return {"total_30h": tot,
            "porsi_pct": {k: round(v / tot * 100, 1) if tot else None for k, v in agg.items()},
            "teratas": rows[:15]}
