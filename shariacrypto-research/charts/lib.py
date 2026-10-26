"""Delapan jenis grafik yang dipakai note APT (22 Okt 2026), digerakkan oleh spec JSON.
Semua fungsi: fn(spec) -> path PNG. Kunci umum spec:
  out, title (kesimpulan), sub, src (sumber + tanggal data), h (tinggi inci),
  notes:  [{x, y, text, color, ha, va, size, bold}]  anotasi bebas (koordinat data)
  hlines: [{y, text, color, ls}] · vlines: [{x, text, color, y}] · spans: [{x0, x1, color, text}]
Lihat charts/examples_APT.json untuk contoh lengkap tiap jenis.
"""
from __future__ import annotations
import csv, datetime as dt
import numpy as np
import matplotlib.dates as md
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter
from .style import BG, GRID, TXT, MUT, G, Y, R, B, O, col, idr, usd_short, setup, frame, save


def _d(s):
    return dt.date.fromisoformat(s) if isinstance(s, str) else s


def _xv(x, dates):
    return _d(x) if dates else x


def _extras(ax, s, dates=False):
    for h in s.get("hlines", []):
        ax.axhline(h["y"], color=col(h.get("color", "MUT")), lw=1.3, ls=h.get("ls", "--"))
        if h.get("text"):
            ax.text(h.get("tx", ax.get_xlim()[1]), h.get("ty", h["y"]), h["text"], color=col(h.get("color", "MUT")),
                    fontsize=8.5, ha=h.get("ha", "right"), va=h.get("va", "bottom"))
    for v in s.get("vlines", []):
        x = _xv(v["x"], dates)
        ax.axvline(x, color=col(v.get("color", "MUT")), lw=.9, ls=":")
        if v.get("text"):
            ax.text(x, v.get("y", ax.get_ylim()[1] * 0.97), v["text"], color=col(v.get("color", "MUT")),
                    fontsize=7.6, ha=v.get("ha", "right"), va="top")
    for sp in s.get("spans", []):
        x0, x1 = _xv(sp["x0"], dates), _xv(sp["x1"], dates)
        ax.axvspan(x0, x1, color=col(sp.get("color", "MUT")), alpha=.12)
        if sp.get("text"):
            xm = x0 + (x1 - x0) / 2
            ax.text(xm, sp.get("y", ax.get_ylim()[1] * 0.9), sp["text"], color=col(sp.get("color", "MUT")),
                    fontsize=7.6, ha="center", va="top")
    for n in s.get("notes", []):
        ax.text(_xv(n["x"], dates), n["y"], n["text"], color=col(n.get("color", "TXT")),
                fontsize=n.get("size", 8.5), ha=n.get("ha", "left"), va=n.get("va", "center"),
                fontweight="bold" if n.get("bold") else "normal", rotation=n.get("rot", 0))


def _fmt_y(ax, kind, d=0):
    f = {"usd": lambda v, p: usd_short(v, d), "pct": lambda v, p: ("+" if v > 0 else "") + idr(v, d) + "%",
         "num": lambda v, p: idr(v, d), "usd_price": lambda v, p: "$" + idr(v, d)}[kind]
    ax.yaxis.set_major_formatter(FuncFormatter(f))


def read_csv_series(path, xcol=0, ycols=(1,)):
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.reader(fh))[1:]
    return [r[xcol] for r in rows], [[float(r[c]) if r[c] not in ("", "None") else np.nan for r in rows] for c in ycols]


# 1. Garis indeks / deret waktu (mis. APT vs BTC = 100) -------------------------------
def line(s):
    """series: [{label, color, x:[tgl], y:[..]} atau {label, color, csv, col}], yfmt, end_labels"""
    fig, ax = setup(h=s.get("h", 3.6))
    ends = []
    for se in s["series"]:
        if "csv" in se:
            xs, (ys,) = read_csv_series(se["csv"], 0, (se.get("col", 1),))
        else:
            xs, ys = se["x"], se["y"]
        xs = [_d(x) for x in xs]
        if s.get("index"):
            base = next(v for v in ys if v == v)
            ys = [v / base * 100 for v in ys]
        ax.plot(xs, ys, color=col(se.get("color")), lw=se.get("lw", 2.2), ls=se.get("ls", "-"))
        ends.append((xs[-1], ys[-1], se))
    if s.get("ylim"):
        ax.set_ylim(*s["ylim"])
    pad = dt.timedelta(days=s.get("pad_days", 45))
    ax.set_xlim(ends[0][0] - dt.timedelta(days=s.get("days", 365)) if s.get("days") else None, ends[0][0] + pad)
    for x, y, se in ends:
        lab = se["label"]
        if s.get("end_labels", True):
            v = (y - 100) if s.get("index") else y
            lab += " " + (("+" if v > 0 else "") + idr(v, 0) + "%" if s.get("index") else idr(v, s.get("d", 2)))
        ax.text(x + dt.timedelta(days=4), y, lab, color=col(se.get("color")), fontsize=8.5,
                va="center", fontweight="bold")
    ax.xaxis.set_major_formatter(md.DateFormatter("%b %y"))
    _fmt_y(ax, s.get("yfmt", "num"), s.get("yd", 0))
    _extras(ax, s, dates=True)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 2. Batang vertikal (mis. unlock per 12 bulan) ----------------------------------------
def bars(s):
    """cats, values, colors (per batang atau satu), labels (opsional teks di atas batang)"""
    fig, ax = setup(h=s.get("h", 3.4), rect=(0.095, 0.19, 0.865, 0.56))
    n = len(s["values"])
    cs = s.get("colors") or [s.get("color", "G")] * n
    ax.bar(range(n), s["values"], color=[col(c) for c in cs], width=.62)
    top = max(s["values"])
    for i, v in enumerate(s["values"]):
        lab = (s.get("labels") or [None] * n)[i] or idr(v, s.get("d", 0))
        ax.text(i, v + top * .02, lab, color=TXT, ha="center", fontsize=9, fontweight="bold")
    ax.set_xticks(range(n))
    ax.set_xticklabels(s["cats"], fontsize=8.5, color=MUT)
    ax.set_ylim(0, s.get("ymax", top * 1.15))
    _fmt_y(ax, s.get("yfmt", "num"))
    _extras(ax, s)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 3. Batang horizontal berlabel (mis. fee 30 hari per aplikasi + kelas syariah) --------
def hbars(s):
    """items: [{label, value, color, text}] urut dari terbesar; label ditulis di atas batang"""
    fig, ax = setup(h=s.get("h", 3.4), grid="x")
    items = s["items"][::-1]
    mx = max(i["value"] for i in items)
    for k, it in enumerate(items):
        ax.barh(k, it["value"], color=col(it.get("color")), height=.42)
        ax.text(it["value"] + mx * .012, k, it.get("text") or usd_short(it["value"]), color=TXT,
                va="center", fontsize=9, fontweight="bold")
        ax.text(mx * .005, k + .26, it["label"], color=MUT, fontsize=8.5, va="bottom")
    ax.set_yticks([])
    ax.set_xlim(0, mx * 1.2)
    ax.set_ylim(-.5, len(items) - .1)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: usd_short(v)))
    _extras(ax, s)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 4. Sebar log-log valuasi (MC vs pendapatan holder; garis lama balik modal) -----------
def scatter_val(s):
    """points: [{label, x (pendapatan/th), y (MC), color, big, left}], payback: [100, 1000, ...]"""
    fig, ax = setup(h=s.get("h", 3.45), rect=(0.095, 0.21, 0.865, 0.55), grid="both")
    ax.grid(color=GRID, lw=.6)
    xl, yl = s.get("xlim", [2e3, 3e8]), s.get("ylim", [2e8, 1e12])
    xx = np.logspace(np.log10(xl[0]), np.log10(xl[1]), 50)
    for m in s.get("payback", [100, 1000, 10000, 100000]):
        ax.plot(xx, xx * m, color=MUT, lw=.8, ls=":")
        xt = min(xl[1] / 2, yl[1] / m / 2)
        if xt > xl[0]:
            ax.text(xt, xt * m * .55, f"{idr(m, 0)} th", color=MUT, fontsize=7.5, rotation=24, ha="right")
    for p in s["points"]:
        c = col(p.get("color"))
        ax.plot([p["x"]], [p["y"]], "o", ms=9 if p.get("big") else 7, color=c, mec=BG)
        left = p.get("left")
        ax.text(p["x"] * (0.75 if left else 1.3), p["y"], p["label"], color=c, fontsize=8.8,
                fontweight="bold", ha="right" if left else "left", va="center")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(*xl); ax.set_ylim(*yl)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: usd_short(v)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: usd_short(v)))
    ax.set_xlabel(s.get("xlabel", "Pendapatan holder per tahun (skala log)"), color=MUT, fontsize=9)
    ax.set_ylabel(s.get("ylabel", "Market cap (skala log)"), color=MUT, fontsize=9)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 5. Kipas skenario 12 bulan (tebal garis = peluang) -----------------------------------
def fan(s):
    """price, scenarios: [{name, target, prob, color}], expected, zone: [lo, hi], months"""
    fig, ax = setup(h=s.get("h", 3.5))
    P, M = s["price"], s.get("months", 12)
    d = s.get("d", 3)
    for sc in s["scenarios"]:
        c, t, p = col(sc.get("color")), sc["target"], sc["prob"]
        ax.plot([0, M], [P, t], color=c, lw=2 + 6 * p, alpha=.85, solid_capstyle="round")
        ch = (t / P - 1) * 100
        ax.text(M + .25, t, f"{sc['name']} ${idr(t, d)}  ({'+' if ch > 0 else ''}{idr(ch, 0)}%) · peluang {round(p * 100)}%",
                color=c, fontsize=9, va="center", fontweight="bold")
    if s.get("expected"):
        e = s["expected"]
        ax.plot([0, M], [P, e], color=TXT, lw=1.4, ls="--")
        yr = s.get("ylim", [0, 1])
        ax.text(M * .5, P + (e - P) * .5 + (yr[1] - yr[0]) * s.get("exp_dy", -.06), f"Harga Perkiraan ${idr(e, d)} ({'+' if e > P else ''}{idr((e / P - 1) * 100, 0)}%)",
                color=TXT, fontsize=8.5)
    ax.plot([0], [P], "o", ms=9, color=TXT)
    ax.text(-.3, P, f"Kini\n${idr(P, d)}", color=TXT, fontsize=9, ha="right", va="center")
    if s.get("zone"):
        lo, hi = s["zone"]
        ax.axhspan(lo, hi, color=Y, alpha=.12)
        ax.text(.4, lo, f"Zona beli ${idr(lo, 2)}–{idr(hi, 2)}", color=Y, fontsize=8.5, va="top")
    ax.set_xlim(-2, M + 10)
    if s.get("ylim"):
        ax.set_ylim(*s["ylim"])
    ticks = s.get("xticks", ["Kini", "+3 bln", "+6 bln", "+9 bln", "+12 bln"])
    ax.set_xticks(np.linspace(0, M, len(ticks)))
    ax.set_xticklabels(ticks, color=MUT)
    _fmt_y(ax, "usd_price", 2)
    _extras(ax, s)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 6. Proyeksi suplai menuju batas (garis lurus per laju bersih) -------------------------
def projection(s):
    """start_year, start_supply, cap, lines: [{label, net_per_year, color, ls}] (satuan sama, mis. juta)"""
    fig, ax = setup(h=s.get("h", 3.6))
    y0, S0, cap = s["start_year"], s["start_supply"], s["cap"]
    end = s.get("end_year", 2100)
    yrs = np.arange(y0, end + 1)
    ax.axhline(cap, color=R, lw=1.4)
    ax.text(y0 + 1, cap * 1.015, s.get("cap_label", f"Batas {idr(cap, 0)}"), color=R, fontsize=9, fontweight="bold")
    for ln in s["lines"]:
        n, c = ln["net_per_year"], col(ln.get("color"))
        y = np.minimum(S0 + n * (yrs - y0), cap)
        ax.plot(yrs, y, color=c, lw=2.2, ls=ln.get("ls", "-"))
        if n > 0:
            hit = y0 + (cap - S0) / n
            if hit <= end:
                ax.plot([hit], [cap], "o", ms=6, color=c)
                ax.text(hit, cap * .975, f"±{int(round(hit))}", color=c, fontsize=8.5, ha="center", va="top")
        lx = ln.get("label_x", min(end - 5, y0 + (end - y0) * .6))
        ly = min(S0 + n * (lx - y0), cap)
        ax.text(lx, ly - (cap - S0) * .03, ln["label"], color=c, fontsize=8.5, va="top")
    ax.set_xlim(y0, end + s.get("pad", 10))
    ax.set_ylim(S0 * .9, cap * 1.07)
    _fmt_y(ax, "num")
    if s.get("ydiv"):
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: idr(v / s["ydiv"], 1) + s.get("ysuf", "")))
    _extras(ax, s)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 7. Titik impas suplai (issuance vs pembakaran per transaksi), sumbu x log -------------
def breakeven(s):
    """issuance_per_year, burn_per_tx, supply, tx_now, x_range: [min, max],
    old: {issuance_per_year, burn_per_tx, label} opsional, bands: [{x0, x1, text, color}]"""
    fig, ax = setup(h=s.get("h", 4.4), rect=(0.08, 0.14, 0.88, 0.66))
    lo, hi = s.get("x_range", [5e6, 3e9])
    tx = np.logspace(np.log10(lo), np.log10(hi), 500)
    S0 = s["supply"]
    f = lambda iss, b: (iss - tx * 365 * b) / S0 * 100
    now = f(s["issuance_per_year"], s["burn_per_tx"])
    ax.axhline(0, color=MUT, lw=1)
    ax.fill_between(tx, now, 0, where=now < 0, color=G, alpha=.12)
    if s.get("old"):
        o = s["old"]
        ax.plot(tx, f(o["issuance_per_year"], o["burn_per_tx"]), color=MUT, lw=1.6, ls=(0, (6, 3, 1, 3)), label=o["label"])
        bp = o["issuance_per_year"] / (365 * o["burn_per_tx"])
        if lo < bp < hi:
            ax.plot([bp], [0], "o", ms=8, mfc=BG, mec=MUT, mew=2.2, zorder=5)
    ax.plot(tx, now, color=G, lw=2.6, label=s.get("label", "Aturan kini"))
    be = s["issuance_per_year"] / (365 * s["burn_per_tx"])
    ax.plot([be], [0], "o", ms=8, mfc=BG, mec=Y, mew=2.2, zorder=5)
    ax.text(be, .8, f"Impas ±{usd_short(be)[1:]}/hari\n(±{idr(be / s['tx_now'], 0)}× hari ini)", color=Y,
            fontsize=9, ha="center", fontweight="bold")
    yn = (s["issuance_per_year"] - s["tx_now"] * 365 * s["burn_per_tx"]) / S0 * 100
    ax.plot([s["tx_now"]], [yn], "o", ms=8, mfc=BG, mec=G, mew=2.2, zorder=5)
    ax.text(s["tx_now"], yn + .7, f"Kini: {usd_short(s['tx_now'], 1)[1:]} transaksi/hari\nsuplai {'+' if yn > 0 else ''}{idr(yn, 1)}%/th",
            color=TXT, fontsize=9)
    for bd in s.get("bands", []):
        ax.axvspan(bd["x0"], bd["x1"], color=col(bd.get("color", "B")), alpha=.07)
        ax.text((bd["x0"] * bd["x1"]) ** .5, s.get("ylim", [-10, 5])[0] * .86, bd["text"],
                color=col(bd.get("color", "B")), fontsize=8, ha="center")
    ax.set_xscale("log")
    ax.set_xlim(lo, hi)
    ax.set_ylim(*s.get("ylim", [-10, 5]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: usd_short(v)[1:]))
    _fmt_y(ax, "pct")
    ax.set_xlabel("Transaksi per hari (skala log)", color=MUT)
    ax.legend(loc="lower left", frameon=False, labelcolor=TXT, fontsize=8.5, bbox_to_anchor=(0, .08))
    _extras(ax, s)
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


# 8. Peta suplai (baris kotak bertingkat) --------------------------------------------
def supplymap(s):
    """cap, cap_label, rows: [[{w, label, sub, color, start(opsional)}...], ...] dari atas ke bawah,
    side_notes: [{text, color}] ditulis di kanan baris terbawah. Satuan bebas (mis. juta)."""
    fig = __import__("matplotlib.pyplot").pyplot.figure(figsize=(10, s.get("h", 5.6)), dpi=150)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.035, 0.08, 0.93, 0.74])
    ax.set_facecolor(BG); ax.axis("off")
    cap = s["cap"]
    ax.set_xlim(0, cap); ax.set_ylim(0, 100)
    ax.plot([0, cap], [92, 92], color=MUT, lw=1)
    ax.text(cap / 2, 95, s.get("cap_label", f"BATAS {idr(cap, 0)}"), color=TXT, ha="center", fontsize=10, fontweight="bold")
    nrow = len(s["rows"])
    hgt = 80 / nrow
    for r, row in enumerate(s["rows"]):
        y = 86 - (r + 1) * hgt + 2
        x = 0
        for bx in row:
            x = bx.get("start", x)
            c = col(bx.get("color"))
            ax.add_patch(Rectangle((x, y), bx["w"], hgt - 6, fc=c, alpha=bx.get("alpha", .18), lw=0))
            ax.add_patch(Rectangle((x, y), bx["w"], hgt - 6, ec=c, fc="none", lw=1.8))
            big = bx["w"] > cap * .12
            ax.text(x + bx["w"] / 2, y + (hgt - 6) * (.62 if bx.get("sub") else .5), bx.get("label", ""), color=c,
                    ha="center", va="center", fontsize=11 if big else 9, fontweight="bold")
            if bx.get("sub"):
                ax.text(x + bx["w"] / 2, y + (hgt - 6) * .28, bx["sub"], color=TXT, ha="center", va="center",
                        fontsize=8.5 if big else 8)
            x += bx["w"]
    yb = 86 - nrow * hgt + 2
    for i, n in enumerate(s.get("side_notes", [])):
        ax.text(s.get("notes_x", cap * .6), yb + (hgt - 6) - 2 - i * 6.5, n["text"], color=col(n.get("color")),
                fontsize=9, va="top")
    frame(fig, s["title"], s.get("sub"), s["src"])
    return save(fig, s["out"])


TYPES = {"line": line, "bars": bars, "hbars": hbars, "scatter_val": scatter_val, "fan": fan,
         "projection": projection, "breakeven": breakeven, "supplymap": supplymap}
