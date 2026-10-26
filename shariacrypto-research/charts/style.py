"""Gaya baku grafik (PANDUAN v3.2 §5.2). Warna hanya untuk makna."""
from __future__ import annotations
import base64, io
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

BG, GRID, TXT, MUT = "#072E1A", "#1E4A2A", "#E8F0EA", "#8FA89A"
G, Y, R, B, O = "#16C784", "#FFC107", "#FF8A8A", "#40C4FF", "#EF9F27"
COLORS = {"hijau": G, "kuning": Y, "merah": R, "biru": B, "oranye": O, "abu": MUT, "putih": TXT,
          "G": G, "Y": Y, "R": R, "B": B, "O": O, "MUT": MUT, "TXT": TXT}
# Makna warna: hijau = baik/halal/aset yang dibahas · merah = buruk/non-halal/risiko ·
# kuning = ambang/zona/BTC · biru = pembanding netral · oranye = perlu perhatian · abu = konteks/lama

_FONT_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"
for _f in _FONT_DIR.glob("*.otf"):  # Inter dibundel (lisensi OFL) agar sama di semua mesin
    try:
        fm.fontManager.addfont(str(_f))
    except Exception:
        pass
_fonts = {f.name for f in fm.fontManager.ttflist}
plt.rcParams.update({"font.family": "Inter" if "Inter" in _fonts else "DejaVu Sans",
                     "font.size": 10, "axes.unicode_minus": False})


def col(c):
    return COLORS.get(c, c) if c else TXT


def idr(x, d=1):
    """Format angka Indonesia: 1.234,5 dan tanda minus asli."""
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("-", "−")


def usd_short(v, d=0):
    a = abs(v)
    for lim, suf in [(1e12, " T"), (1e9, " M"), (1e6, " jt"), (1e3, " rb")]:
        if a >= lim:
            return "$" + idr(v / lim, d) + suf
    return "$" + idr(v, d)


def setup(h=3.6, w=10, rect=(0.095, 0.15, 0.865, 0.60), grid="y"):
    fig = plt.figure(figsize=(w, h), dpi=150)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes(rect)
    ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=MUT, length=0)
    if grid:
        ax.grid(axis=grid, color=GRID, lw=.8)
    ax.set_axisbelow(True)
    return fig, ax


def frame(fig, title, sub, src):
    """Judul = kesimpulan (bukan nama grafik). Sumber + tanggal data wajib."""
    fig.text(0.035, 0.965, title, color=TXT, fontsize=14.5, fontweight="bold", va="top")
    if sub:
        fig.text(0.035, 0.875, sub, color=MUT, fontsize=8.8, va="top")
    fig.text(0.965, 0.02, src, color=MUT, fontsize=7.3, ha="right")


def save(fig, path: str | Path, max_kb=100):
    """Simpan PNG lalu kompres ke ≤ max_kb (256 warna FASTOCTREE; turunkan skala bila perlu)."""
    from PIL import Image
    path = Path(path)
    buf = io.BytesIO()
    fig.savefig(buf, facecolor=BG, format="png")
    plt.close(fig)
    im = Image.open(io.BytesIO(buf.getvalue())).convert("RGB")
    scale = 1.0
    while True:
        w, h = int(im.width * scale), int(im.height * scale)
        q = im.resize((w, h), Image.LANCZOS) if scale < 1 else im
        q = q.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
        out = io.BytesIO()
        q.save(out, format="PNG", optimize=True)
        if out.tell() <= max_kb * 1024 or scale < 0.55:
            break
        scale -= 0.08
    path.write_bytes(out.getvalue())
    return path


def data_uri(path: str | Path) -> str:
    return "data:image/png;base64," + base64.b64encode(Path(path).read_bytes()).decode()
