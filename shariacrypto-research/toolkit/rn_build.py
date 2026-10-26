# -*- coding: utf-8 -*-
"""
Shariacrypto Research Note builder.

Usage:
    python3 rn_build.py content.json rn_shell.html output.html

content.json  : isi note (lihat PANDUAN.md dan contoh_ETH.json)
rn_shell.html : cangkang halaman (CSS brand, font, logo, editor "Edit isi / Simpan PDF")
output.html   : file siap diterbitkan sebagai artifact

Semua teks boleh berisi HTML inline sederhana (<strong>, <br>, &amp;, &lt;).
Warna yang dikenali: green, gold, orange, red, info, muted, white, warning, body.
"""
import json, re, sys

COL = {'green': 'var(--success-solid)', 'gold': 'var(--gold-500)', 'orange': 'var(--warning-solid)', 'red': 'var(--danger)',
       'info': 'var(--info)', 'muted': 'var(--text-muted)', 'white': 'var(--white)', 'warning': 'var(--warning)', 'body': 'var(--text-body)',
       'blue': 'var(--info)', 'darkred': 'var(--danger-solid)'}
BG = {'green': 'var(--success-bg)', 'gold': 'var(--warning-bg)', 'warning': 'var(--warning-bg)', 'orange': 'var(--warning-bg)', 'red': 'var(--danger-bg)',
      'info': 'var(--info-bg)', 'muted': 'rgba(139,143,168,0.12)', 'white': 'rgba(255,255,255,0.08)', 'body': 'rgba(139,143,168,0.12)', 'blue': 'var(--info-bg)'}
MONO = 'font-family: var(--font-mono);'
PAGE_STYLE = ('position: relative; width: 794px; height: 1123px; box-sizing: border-box; padding: 40px 44px 0px; '
              'background-color: var(--bg-base); background-image: var(--bg-bloom-tr); box-shadow: var(--shadow-lg); '
              'overflow: hidden; font-family: var(--font-sans); color: var(--text-body); font-size: 11px; line-height: 1.55; scroll-margin-top: 72px;')


def c(name, default='body'):
    if not name:
        name = default
    return COL.get(name, name)


def bg(name):
    return BG.get(name or 'muted', name)


# Angka dan satuannya tidak dipisah ke baris berbeda ("$1,44 miliar", "±420 th").
_SATUAN = re.compile(r'(\d)[ \u00a0]+(juta|miliar|triliun|ribu|jt|rb|th|bln|M|T|B|K)\b')


def nb(t):
    return _SATUAN.sub(lambda m: m.group(1) + '&nbsp;' + m.group(2), t) if isinstance(t, str) else t


# Emoji status diganti ikon garis (gaya tools/ikon.py: 24px, garis 1,8).
_IK = {
    'cek': ('var(--success-solid)', '<path d="m5 12.5 4.5 4.5L19 7.5"/>'),
    'awas': ('var(--warning)', '<path d="M12 4 2.8 19.5h18.4z"/><path d="M12 10v4.3M12 16.8v.2"/>'),
    'silang': ('var(--danger)', '<path d="M7 7l10 10M17 7 7 17"/>'),
}
_EMOJI = {'\u2705': 'cek', '\u2714\ufe0f': 'cek', '\u2714': 'cek', '\u26a0\ufe0f': 'awas', '\u26a0': 'awas', '\u274c': 'silang', '\u274e': 'silang', '\u26d4': 'silang'}


def ikon(nama, size=11):
    col, d = _IK[nama]
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" style="display: inline-block; vertical-align: -1px;">{d}</svg>')


def ikonkan(html):
    for e, n in _EMOJI.items():
        html = html.replace(e, ikon(n))
    return html


def wh(t):
    return f'<strong style="color: var(--white);">{t}</strong>'


# ------------------------------------------------------------------ primitives
def ed(t, style=''):
    return f'<div data-ed="1" style="text-wrap: pretty;{style}">{t}</div>'


def lbl(t, color='muted'):
    return f'<div style="{MONO} font-size: 8.5px; letter-spacing: 0.08em; color: {c(color)}; margin-bottom: 3px;">{t}</div>'


def note(t):
    return ed(t, ' font-size: 9px; color: var(--text-muted); margin-top: 3px; line-height: 1.45;')


def pill(t, color='muted'):
    return f'<span data-ed="1" style="{MONO} font-size: 9px; padding: 2px 8px; border-radius: 999px; color: {c(color)}; background: {bg(color)}; white-space: nowrap;">{t}</span>'


def dot(color):
    return f'<span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: {c(color)}; margin-right: 5px;"></span>'


def status(color, t):
    """Pill status bertitik dengan latar tipis (sama dengan badge situs)."""
    return (f'<span style="display: inline-flex; align-items: center; gap: 5px; font-size: 9px; font-weight: 600; line-height: 1.5; color: {c(color)}; '
            f'background: {bg(color)}; border-radius: 999px; padding: 0px 8px 0px 6px; white-space: nowrap;">'
            f'<span style="width: 6px; height: 6px; border-radius: 50%; background: {c(color)};"></span>{t}</span>')


def chip(t, color='muted', with_dot=False):
    d = f'<span style="width: 7px; height: 7px; border-radius: 50%; background: {c(color)}; flex: 0 0 auto;"></span>' if with_dot else ''
    return (f'<span data-ed="1" style="display: inline-flex; align-items: center; gap: 7px; font-family: var(--font-sans); font-weight: 600; font-size: 11.5px; '
            f'letter-spacing: 0.04em; line-height: 1.4; color: {c(color)}; background: {bg(color)}; border-radius: var(--r-pill); padding: 4px 11px; white-space: nowrap;">{d}{t}</span>')


def cell(v, align='l', head=False):
    """Table cell. v = str (html) | {"n": value, "c": color, "b": bold, "s": small-note} | {"t": label, "s": sub, "c": color} | {"dot": color, "t": text}"""
    ta = 'text-align: right;' if align == 'r' else ('text-align: center;' if align == 'c' else '')
    attr = '' if head else ' data-ed="1"'
    if isinstance(v, dict):
        s = f'<span style="display: block; font-size: 8.5px; color: var(--text-muted); line-height: 1.35;">{v["s"]}</span>' if v.get('s') else ''
        if 'n' in v:
            inner = f'<span style="{MONO} font-variant-numeric: tabular-nums; color: {c(v.get("c"), "body")};{" font-weight: 700;" if v.get("b") else ""}">{nb(v["n"])}</span>' + s
        elif 'dot' in v:
            t = v.get('t', '')
            # label status pendek -> pill; kalimat panjang tetap titik + teks
            inner = (status(v['dot'], t) if len(re.sub(r'<[^>]+>', '', t)) <= 22 else dot(v['dot']) + t) + s
        else:
            inner = f'<strong style="color: {c(v.get("c"), "white")};">{v.get("t", "")}</strong>' + s
        return f'<span{attr} style="{ta}">{inner}</span>'
    return f'<span{attr} style="{ta}">{v if v is not None else ""}</span>'


# ------------------------------------------------------------------ blocks
def b_bigsec(b):
    return (f'<div style="display: flex; align-items: baseline; gap: 10px; margin: {b.get("mt", 16)}px 0px 4px;">'
            f'<span style="font-size: 21px; font-weight: 800; letter-spacing: -0.02em; color: var(--success-solid);">{b["num"]}</span>'
            f'<span data-ed="1" style="font-weight: 800; font-size: 21px; letter-spacing: -0.025em; line-height: 1.15; color: var(--white);">{b["title"]}</span></div>')


def b_sub(b):
    r = f'<span data-ed="1" style="margin-left: auto; color: var(--text-muted); letter-spacing: 0.04em;">{b["right"]}</span>' if b.get('right') else ''
    return (f'<div style="display: flex; gap: 8px; {MONO} font-size: 9px; letter-spacing: 0.1em; color: var(--text-body); margin: {b.get("mt", 14)}px 0px {b.get("mb", 8)}px; padding-bottom: 6px; border-bottom: 1px solid var(--border-strong);">'
            f'<span style="color: var(--success-solid);">{b.get("num", "")}</span><span data-ed="1">{b["title"]}</span>{r}</div>')


def b_text(b):
    st = ''
    if b.get('muted'):
        st += ' color: var(--text-muted);'
    if b.get('size'):
        st += f' font-size: {b["size"]}px;'
    if b.get('mt') is not None:
        st += f' margin-top: {b["mt"]}px;'
    if b.get('mb') is not None:
        st += f' margin-bottom: {b["mb"]}px;'
    return ed(b['html'], st)


def b_note(b):
    return note(b['html'])


def b_formula(b):
    return f'<div data-ed="1" style="margin: 5px 0px 2px; padding: 6px 10px; border: 1px dashed var(--border-strong); border-radius: 6px; {MONO} font-size: 9.5px; color: var(--white); line-height: 1.6;">{b["html"]}</div>'


def _li(items):
    return ''.join(f'<li data-ed="1" style="margin: 0px 0px 3px; text-wrap: pretty;">{i}</li>' for i in items)


def b_ul(b):
    return f'<ul style="margin: 0px; padding-left: 15px;">{_li(b["items"])}</ul>'


def b_ol(b):
    return f'<ol style="margin: 0px; padding-left: 16px;">{_li(b["items"])}</ol>'


def b_table(b):
    n = len(b['header'])
    align = b.get('align') or ['l'] * n
    cols = b['cols']
    hl = b.get('hl', [])
    hl = hl if isinstance(hl, list) else [hl]
    size = b.get('size', 10)
    h = (f'<div style="display: grid; grid-template-columns: {cols}; gap: 8px; padding: 6px 10px; background: var(--surface-card); {MONO} font-size: 8.5px; letter-spacing: 0.06em; color: var(--text-muted);">'
         + ''.join(cell(x, align[i], True) for i, x in enumerate(b['header'])) + '</div>')
    body = ''
    for ri, r in enumerate(b['rows']):
        bgc = 'var(--success-bg)' if ri in hl else 'transparent'
        body += (f'<div style="display: grid; grid-template-columns: {cols}; gap: 8px; align-items: baseline; padding: {b.get("pad", 5)}px 10px; border-top: 1px solid var(--border); background: {bgc}; font-size: {size}px;">'
                 + ''.join(cell(x, align[i]) for i, x in enumerate(r)) + '</div>')
    mt = f' margin-top: {b["mt"]}px;' if b.get('mt') is not None else ''
    return f'<div style="border: 1px solid var(--border); border-radius: var(--r-md); overflow: hidden;{mt}">{h}{body}</div>'


def b_mtab(b):
    cols, hl = b['cols'], b.get('hl')
    out = '<div style="margin: 5px 0px 3px; border: 1px solid var(--border); border-radius: 6px; overflow: hidden;">'
    out += (f'<div style="display: grid; grid-template-columns: {cols}; gap: 8px; padding: 4px 8px; background: var(--bg-alt); {MONO} font-size: 8px; letter-spacing: 0.05em; color: var(--text-muted);">'
            + ''.join(f'<span style="{"text-align: right;" if j else ""}">{x}</span>' for j, x in enumerate(b['header'])) + '</div>')
    for i, r in enumerate(b['rows']):
        bgc = 'var(--success-bg)' if hl is not None and i == hl else 'transparent'
        out += (f'<div style="display: grid; grid-template-columns: {cols}; gap: 8px; padding: 3px 8px; border-top: 1px solid var(--border); font-size: {b.get("size", 9.5)}px; background: {bgc};">'
                + ''.join(f'<span data-ed="1" style="{"text-align: right; " + MONO + " font-variant-numeric: tabular-nums;" if j else ""}">{nb(x) if j else x}</span>' for j, x in enumerate(r)) + '</div>')
    return out + '</div>'


def b_card(b):
    inner = (lbl(b['label'], b.get('label_color', 'muted')) if b.get('label') else '') + blocks(b.get('blocks', []))
    extra = ''
    if b.get('mt') is not None:
        extra += f' margin-top: {b["mt"]}px;'
    if b.get('accent'):
        extra += f' border-top: 3px solid {c(b["accent"])};'
    return f'<div style="padding: 10px 12px; background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-md);{extra}">{inner}</div>'


def b_grid(b):
    mt = b.get('mt', 10)
    return (f'<div style="display: grid; grid-template-columns: {b.get("cols", "minmax(0px,1fr) minmax(0px,1fr)")}; gap: {b.get("gap", 12)}px; margin-top: {mt}px; align-items: {b.get("align", "stretch")};">'
            + ''.join(f'<div style="min-width: 0px; display: flex; flex-direction: column;">{blocks(it if isinstance(it, list) else [it])}</div>' for it in b['items']) + '</div>')


def b_kv(b):
    out = ''
    for row in b['rows']:
        k, v = row[0], row[1]
        col = row[2] if len(row) > 2 else 'body'
        out += (f'<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; padding: 3px 0px; border-bottom: 1px solid var(--border); font-size: 9.5px;">'
                f'<span style="color: var(--text-muted);">{k}</span><span data-ed="1" style="{MONO} font-variant-numeric: tabular-nums; color: {c(col)}; font-weight: 500; text-align: right;">{nb(v)}</span></div>')
    return out


def b_h9(b):
    r = f'<span data-ed="1" style="margin-left: auto; color: var(--text-muted);">{b["right"]}</span>' if b.get('right') else ''
    return (f'<div style="display: flex; gap: 8px; {MONO} font-size: 9px; letter-spacing: 0.1em; color: var(--text-body); padding-bottom: 5px; '
            f'border-bottom: 1px solid var(--border-strong); margin: {b.get("mt", 0)}px 0px {b.get("mb", 6)}px;"><span style="color: var(--success-solid);">{b.get("num", "")}</span><span data-ed="1">{b["title"]}</span>{r}</div>')


def b_thesis(b):
    rows = b['rows']
    return ''.join(f'<div style="display: grid; grid-template-columns: 58px 1fr; gap: 10px; padding: 4px 0px;{"" if i == len(rows) - 1 else " border-bottom: 1px solid var(--border);"}">'
                   f'<div style="{MONO} font-size: 9px; color: var(--success-solid); padding-top: 2px;">{k}</div>{ed(v)}</div>' for i, (k, v) in enumerate(rows))


def b_srows(b):
    out = ''
    rows = b['rows']
    for i, r in enumerate(rows):
        bd = '' if i == len(rows) - 1 else ' border-bottom: 1px solid var(--border);'
        tc = r.get('tagc', 'green')
        out += (f'<div style="display: grid; grid-template-columns: 24px 1fr auto; gap: 9px; align-items: start; padding: 5px 0px;{bd}">'
                f'<span style="{MONO} font-size: 9px; color: {c(tc)}; background: {bg(tc)}; border-radius: 4px; text-align: center; padding: 1px 0px;">{r["tag"]}</span>'
                f'<div data-ed="1" style="text-wrap: pretty;"><strong style="color: var(--white);">{r["title"]}</strong> — {r["body"]}</div>'
                f'<span data-ed="1" style="{MONO} font-size: 9px; color: {c(r.get("rcolor", "muted"))}; text-align: right; line-height: 1.5;">{r["right"]}</span></div>')
    return out


def b_scen(b):
    """Scenario verdict card (page 1)."""
    rows = ''
    for i, r in enumerate(b['rows']):
        bd = '' if i == len(b['rows']) - 1 else ' border-bottom: 1px solid var(--border);'
        col = c(r['color'])
        rows += (f'<div style="display: grid; grid-template-columns: 46px 44px 62px 56px minmax(0px,1fr); gap: 8px; align-items: baseline; padding: 4px 0px;{bd} font-size: 10px;">'
                 f'<span style="color: {col}; font-weight: 700;">{r["name"]}</span><span data-ed="1" style="{MONO} text-align: right; color: var(--white);">{r["prob"]}</span>'
                 f'<span data-ed="1" style="{MONO} text-align: right; color: {col};">{r["target"]}</span><span data-ed="1" style="{MONO} text-align: right; color: var(--text-muted);">{r["ret"]}</span>'
                 f'<span data-ed="1" style="color: var(--text-muted); font-size: 9.5px;">{r["basis"]}</span></div>')
    return ('<div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-md); padding: 10px 12px;">'
            f'<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;"><span data-ed="1" style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 0.04em; color: {c(b.get("color", "green"))};">{b["label"]}</span>'
            f'<span data-ed="1" style="{MONO} font-size: 10px; color: var(--white);">{b.get("right", "")}</span></div>'
            f'<div style="margin-top: 6px;">{rows}</div>' + (note(b['note']) if b.get('note') else '') + '</div>')


def b_tiles(b):
    """Row of small value tiles (e.g. 2030 prices)."""
    n = len(b['items'])
    return (f'<div style="display: grid; grid-template-columns: repeat({n}, minmax(0px,1fr)); gap: 8px;">' +
            ''.join(f'<div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-md); padding: 7px 10px;">'
                    f'<div style="{MONO} font-size: 8.5px; letter-spacing: 0.06em; color: var(--text-muted);">{it["label"]}</div>'
                    f'<div data-ed="1" style="{MONO} font-weight: 700; font-size: {it.get("size", 13)}px; color: {c(it.get("color", "info"))}; margin-top: 2px;">{it["value"]}</div>'
                    + (f'<div data-ed="1" style="font-size: 9px; color: var(--text-muted);">{it["sub"]}</div>' if it.get('sub') else '') + '</div>'
                    for it in b['items']) + '</div>')


def b_tgt(b):
    """Target lens stack (page 1 aside)."""
    heads = b['heads']
    out = f'<div style="display: flex; flex-direction: column; border: 1px solid var(--border); border-radius: var(--r-md); overflow: hidden; {MONO} font-size: 10px; font-variant-numeric: tabular-nums;">'
    for i, r in enumerate(b['rows']):
        bt = 'border-top: 0px;' if i == 0 else 'border-top: 1px solid var(--border);'
        col = c(r['color'])
        vals = ''.join(f'<div style="{"text-align: right;" if j == len(heads) - 1 else ""}">{h}<div data-ed="1" style="color: var(--text-body); font-size: 9.5px;">{nb(r["vals"][j])}</div></div>' for j, h in enumerate(heads))
        out += (f'<div style="padding: 6px 10px; background: {bg(r["color"])}; {bt}">'
                f'<div style="display: flex; align-items: baseline; gap: 8px; color: {col};"><span style="flex: 1 1 0%;">{r["name"]}</span>'
                f'<span data-ed="1" style="font-weight: 700; font-size: 12px;">{r["price"]}</span><span data-ed="1" style="min-width: 44px; text-align: right;">{r["ret"]}</span></div>'
                f'<div style="display: grid; grid-template-columns: repeat({len(heads)}, minmax(0px,1fr)); gap: 6px; margin-top: 4px; padding-top: 4px; border-top: 1px solid var(--border); font-size: 8px; color: var(--text-muted);">{vals}</div></div>')
    return out + '</div>'


def b_bars(b):
    """Horizontal bars on a shared linear scale. rows: [{label, value, color, display}]"""
    mx = b.get('max') or max(r['value'] for r in b['rows'])
    lw = b.get('label_width')
    out = ''
    for r in b['rows']:
        w = max(r['value'] / mx * 100, 0.8)
        if lw:
            out += (f'<div style="display: grid; grid-template-columns: {lw}px minmax(0px,1fr) {b.get("value_width", 104)}px; gap: 10px; align-items: center; margin-top: 5px; font-size: 9.5px;">'
                    f'<span data-ed="1" style="color: var(--white);">{r["label"]}</span>'
                    f'<div title="{r["label"]}: {r["display"]}" style="height: 9px; border-radius: 3px; background: var(--bg-alt); overflow: hidden;"><div style="height: 100%; width: {w:.1f}%; background: {c(r.get("color", "green"))}; border-radius: 3px;"></div></div>'
                    f'<span data-ed="1" style="{MONO} color: var(--text-muted); text-align: right;">{r["display"]}</span></div>')
        else:
            out += (f'<div style="margin-top: 6px;"><div style="display: flex; justify-content: space-between; font-size: 9.5px;"><span data-ed="1" style="color: var(--white);">{r["label"]}</span>'
                    f'<span data-ed="1" style="{MONO} color: var(--text-muted);">{r["display"]}</span></div>'
                    f'<div title="{r["label"]}: {r["display"]}" style="height: 9px; margin-top: 2px; border-radius: 3px; background: var(--bg-alt); overflow: hidden;"><div style="height: 100%; width: {w:.1f}%; background: {c(r.get("color", "green"))}; border-radius: 3px;"></div></div></div>')
    return out


def b_split(b):
    """Single stacked 100% bar with two labels (e.g. app vs chain)."""
    segs = ''.join(f'<div title="{s["label"]}" style="flex: {s["value"]}; background: {c(s.get("color", "green")) if s.get("color") != "dim" else "var(--border-strong)"};"></div>' for s in b['segments'])
    labs = ''.join(f'<span data-ed="1" style="color: {c(s.get("label_color", "muted"))};">{s["label"]}</span>' for s in b['segments'])
    return (f'<div style="display: flex; height: 12px; border-radius: 4px; overflow: hidden; margin: 5px 0px 4px; gap: 2px;">{segs}</div>'
            f'<div style="display: flex; justify-content: space-between; {MONO} font-size: 9px;">{labs}</div>')


def b_sankey(b):
    """One source splitting into 2–4 flows. source: {label, display}; flows: [{label, value, display, color}]"""
    W = b.get('width', 430)
    total = sum(f['value'] for f in b['flows'])
    scale = b.get('height', 126) / total
    x0, x1, nw, top = 118, 300, 11, 22
    hf = total * scale
    gap = 14
    ys, y = [], top - 8
    for f in b['flows']:
        ys.append(y)
        y += f['value'] * scale + gap
    T = lambda x, yy, t, anc='start', col='var(--text-body)', sz=10, w=500, fam='var(--font-sans)': f'<text x="{x}" y="{yy:.1f}" text-anchor="{anc}" fill="{col}" font-size="{sz}" font-weight="{w}" font-family="{fam}">{t}</text>'
    g, cur = [], top
    for f, yb in zip(b['flows'], ys):
        h = f['value'] * scale
        col = c(f.get('color', 'green'))
        cx = (x0 + nw + x1) / 2
        g.append(f'<path d="M{x0 + nw},{cur:.1f} C{cx},{cur:.1f} {cx},{yb:.1f} {x1},{yb:.1f} L{x1},{yb + h:.1f} C{cx},{yb + h:.1f} {cx},{cur + h:.1f} {x0 + nw},{cur + h:.1f} Z" fill="{col}" fill-opacity="0.5"><title>{f["label"]}: {f["display"]}</title></path>')
        g.append(f'<rect x="{x1}" y="{yb:.1f}" width="{nw}" height="{max(h, 2):.1f}" rx="2" fill="{col}"/>')
        g.append(T(x1 + nw + 7, yb + h / 2 - 3, f['label'], 'start', 'var(--white)', 10, 700))
        g.append(T(x1 + nw + 7, yb + h / 2 + 10, f['display'], 'start', c(f.get('display_color', 'muted')), 9, 400, 'var(--font-mono)'))
        cur += h
    g.append(f'<rect x="{x0}" y="{top}" width="{nw}" height="{hf:.1f}" rx="2" fill="var(--info-solid)"/>')
    g.append(T(x0 - 8, top + hf / 2 - 3, b['source']['label'], 'end', 'var(--white)', 10, 700))
    g.append(T(x0 - 8, top + hf / 2 + 10, b['source']['display'], 'end', 'var(--text-muted)', 9, 400, 'var(--font-mono)'))
    H = max(y, top + hf) + 2
    return (f'<svg viewBox="0 0 {W} {H:.0f}" width="100%" role="img" aria-label="{b.get("aria", "Sankey")}" style="display: block;">' + ''.join(g) + '</svg>')


def b_heat(b):
    """Sensitivity grid. values[row][col] numbers; thresholds [low, high]; prefix (default '$'); decimals (default 0)."""
    lo, hi = b['thresholds']
    ncol = len(b['col_labels'])
    pre = b.get('prefix', '$')
    dec = int(b.get('decimals', 0))

    def fmt(v):
        # format Indonesia: titik ribuan, koma desimal (mis. $2.689 atau $0,092)
        if not isinstance(v, (int, float)):
            return str(v)
        return pre + f'{v:,.{dec}f}'.replace(',', '\x00').replace('.', ',').replace('\x00', '.')
    out = (f'<div style="display: grid; grid-template-columns: minmax(0px,1.3fr) repeat({ncol}, minmax(0px,1fr)); gap: 3px; {MONO} font-size: 9.5px; font-variant-numeric: tabular-nums;">'
           f'<span style="font-size: 8px; color: var(--text-muted); letter-spacing: 0.05em; padding: 3px 0px;">{b.get("corner", "")}</span>' +
           ''.join(f'<span style="font-size: 8px; color: var(--text-muted); text-align: center; padding: 3px 0px;">{x}</span>' for x in b['col_labels']))
    for name, vals in zip(b['row_labels'], b['values']):
        out += f'<span data-ed="1" style="color: var(--white); font-family: var(--font-sans); font-size: 9.5px; padding: 2px 0px;">{name}</span>'
        for v in vals:
            if v < lo:
                bgc, fc = 'var(--danger-bg)', COL['red']
            elif v < hi:
                bgc, fc = 'rgba(255,193,7,0.08)', COL['warning']
            else:
                bgc, fc = 'var(--success-bg)', COL['green']
            out += f'<span data-ed="1" title="{fmt(v)}" style="background: {bgc}; color: {fc}; text-align: center; padding: 2px 0px; border-radius: 4px;">{fmt(v)}</span>'
    return out + '</div>'


def b_tree(b):
    out = '<div style="display: flex; flex-direction: column; gap: 6px;">'
    for n in b['nodes']:
        col = c(n['color'])
        out += (f'<div style="border: 1px solid var(--border); border-left: 3px solid {col}; border-radius: 6px; padding: 6px 9px; background: var(--bg-alt);">'
                f'<div style="display: flex; justify-content: space-between; font-weight: 700; color: var(--white);"><span data-ed="1">{n["title"]}</span><span data-ed="1" style="{MONO} color: {col};">{n["prob"]}</span></div>'
                f'<div data-ed="1" style="font-size: 9px; color: var(--text-muted); line-height: 1.45; margin-top: 1px;">{n["sub"]}</div></div>')
    return out + '</div>'


def b_timeline(b):
    return ''.join(f'<div style="display: grid; grid-template-columns: 72px minmax(0px,1fr) 52px; gap: 8px; padding: 4px 0px; border-bottom: 1px solid var(--border); font-size: 9.5px;">'
                   f'<span data-ed="1" style="{MONO} color: var(--text-muted);">{d}</span><span data-ed="1">{t}</span><span data-ed="1" style="{MONO} font-size: 8.5px; color: var(--success-solid); text-align: right;">{k}</span></div>'
                   for d, t, k in b['rows'])


def b_lrow(r, last):
    bd = '' if last else ' border-bottom: 1px solid var(--border);'
    return (f'<div style="display: grid; grid-template-columns: 104px minmax(0px,1fr); gap: 14px; padding: 7px 0px;{bd}">'
            f'<div style="{MONO} font-size: 8.5px; letter-spacing: 0.08em; color: var(--text-muted); padding-top: 2px; line-height: 1.5;">{r["label"]}</div><div>{blocks(r["blocks"])}</div></div>')


def b_dcard(b):
    """Catalyst / risk detail card with label-left rows."""
    acc = c(b.get('accent', 'green'))
    pills = ''.join(pill(p['t'], p.get('c', 'muted')) for p in b.get('pills', []))
    rows = b['rows']
    return (f'<div style="background: var(--surface-card); border: 1px solid var(--border); border-left: 3px solid {acc}; border-radius: var(--r-md); padding: 10px 14px 4px; margin-top: {b.get("mt", 10)}px;">'
            f'<div style="display: flex; align-items: center; gap: 8px;"><span style="{MONO} font-size: 9px; letter-spacing: 0.08em; color: {acc};">{b["tag"]}</span>'
            f'<span style="margin-left: auto; display: flex; gap: 6px;">{pills}</span></div>'
            f'<div data-ed="1" style="font-weight: 700; font-size: {b.get("title_size", 14)}px; color: var(--white); line-height: 1.3; margin-top: 3px;">{b["title"]}</div>'
            + (f'<div data-ed="1" style="color: var(--text-muted); margin-bottom: 2px;">{b["subtitle"]}</div>' if b.get('subtitle') else '')
            + ''.join(b_lrow(r, i == len(rows) - 1) for i, r in enumerate(rows)) + '</div>')


def b_stats(b):
    """Kotak ringkasan skenario dengan kolom angka."""
    n = len(b['items'])
    return ('<div style="margin-top: 10px; background: var(--surface-card); border: 1px solid var(--border-strong); border-radius: var(--r-md); padding: 10px 14px;">'
            f'<div style="display: flex; align-items: baseline; gap: 10px;"><span style="{MONO} font-size: 9px; letter-spacing: 0.08em; color: var(--text-muted);">{b.get("label", "RINGKASAN SKENARIO")}</span>'
            f'<span data-ed="1" style="margin-left: auto; {MONO} font-weight: 700; font-size: 12px; color: {c(b.get("color", "green"))};">{b["verdict"]}</span></div>'
            f'<div style="display: grid; grid-template-columns: repeat({n}, minmax(0px,1fr)); gap: 10px; margin-top: 6px;">' +
            ''.join(f'<div><div style="{MONO} font-size: 8px; letter-spacing: 0.06em; color: var(--text-muted);">{it["label"]}</div><div data-ed="1" style="{MONO} font-size: 15px; font-weight: 700; color: {c(it.get("color", "white"))};">{it["value"]}</div>'
                    f'<div data-ed="1" style="font-size: 9px; color: var(--text-muted);">{it.get("sub", "")}</div></div>' for it in b['items']) + '</div>' +
            (ed(b['note'], ' font-size: 9.5px; margin-top: 5px; color: var(--text-muted);') if b.get('note') else '') + '</div>')


def b_sharia(b):
    def layer(L):
        return (f'<div style="display: grid; grid-template-columns: 104px minmax(0px,1fr) 70px; gap: 12px; align-items: center; padding: 5px 0px; border-bottom: 1px solid var(--border);">'
                f'<div><div style="{MONO} font-size: 8.5px; letter-spacing: 0.08em; color: var(--text-muted);">{L["label"]}</div><div style="font-weight: 700; color: var(--white);">{L["name"]}</div></div>'
                f'<div data-ed="1" style="text-wrap: pretty;"><span style="color: {c(L.get("icon_color", "warning"))};">{L.get("icon", "")}</span> {L["text"]}</div>'
                f'<div style="text-align: right;"><span data-ed="1" style="{MONO} font-size: 10px; color: var(--white);">{L["score"]}</span>'
                f'<div style="height: 4px; border-radius: 999px; background: var(--bg-alt); border: 1px solid var(--border); overflow: hidden; margin-top: 3px;"><div style="height: 100%; width: {L["pct"]}%; background: var(--success-solid);"></div></div></div></div>')
    vc = b.get('verdict_color', 'green')
    return ('<div style="display: grid; grid-template-columns: 158px minmax(0px,1fr); gap: 16px; margin-top: 6px; align-items: start;">'
            '<div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 12px;">'
            f'<div style="{MONO} font-size: 8.5px; letter-spacing: 0.08em; color: var(--text-muted);">{b.get("score_label", "SKOR SYARIAH")}</div>'
            + skor_cincin(b['score'], vc, b['verdict'])
            + skor_ambang(b['score']) + gerbang(b['layers'])
            + ed(b.get('summary', ''), ' font-size: 9px; color: var(--text-muted); margin-top: 8px; padding-top: 6px; border-top: 1px solid var(--border);') +
            '</div><div>' + ''.join(layer(L) for L in b['layers']) + blocks(b.get('after', [])) + '</div></div>')


def _angka(t):
    m = re.search(r'\d+(?:[.,]\d+)?', str(t))
    return float(m.group(0).replace(',', '.')) if m else None


def skor_cincin(score, color, verdict):
    """Cincin skor 0–100 seperti kartu Status Syariah di screener."""
    v = _angka(score) or 0
    r, k = 30, 2 * 3.14159 * 30
    return ('<div style="display: flex; align-items: center; gap: 10px; margin-top: 8px;">'
            f'<svg viewBox="0 0 72 72" width="72" height="72" role="img" aria-label="Skor syariah {score} dari 100" style="flex: 0 0 auto;">'
            f'<circle cx="36" cy="36" r="{r}" fill="none" stroke="var(--border)" stroke-width="7"/>'
            f'<circle cx="36" cy="36" r="{r}" fill="none" stroke="{c(color)}" stroke-width="7" stroke-linecap="round" '
            f'stroke-dasharray="{k * min(v, 100) / 100:.1f} {k:.1f}" transform="rotate(-90 36 36)"/>'
            f'<text x="36" y="40" text-anchor="middle" fill="var(--white)" font-size="19" font-weight="700" font-family="var(--font-mono)">{score}</text>'
            '<text x="36" y="52" text-anchor="middle" fill="var(--text-muted)" font-size="7" font-family="var(--font-sans)">dari 100</text></svg>'
            f'<div data-ed="1" style="font-weight: 800; font-size: 13px; line-height: 1.2; letter-spacing: -0.01em; color: {c(color)};">{verdict}</div></div>')


def skor_ambang(score):
    """Bar 0–100 dengan ambang 40/60/80 dan penanda skor."""
    v = max(0, min(_angka(score) or 0, 100))
    ticks = ''.join(f'<span style="position: absolute; left: {x}%; transform: translateX(-50%);">{x}</span>' for x in (40, 60, 80))
    return ('<div style="margin-top: 10px;">'
            '<div style="position: relative; height: 6px; border-radius: 999px; background: linear-gradient(90deg, var(--danger) 0 40%, var(--warning-solid) 40% 60%, var(--gold-500) 60% 80%, var(--success-solid) 80% 100%); opacity: 0.9;">'
            f'<span style="position: absolute; left: {v}%; top: -3px; width: 3px; height: 12px; margin-left: -1.5px; border-radius: 2px; background: var(--white); box-shadow: 0 0 0 1.5px var(--bg-base);"></span></div>'
            f'<div style="position: relative; height: 11px; margin-top: 2px; {MONO} font-size: 7.5px; color: var(--text-muted);">{ticks}</div></div>')


GERBANG = ((0, 'L1', 12), (2, 'L3', 4), (3, 'L4', 12))


def gerbang(layers):
    """Chip gerbang L1/L3/L4 dihitung dari skor lapis ("26/30")."""
    if len(layers) != 4:
        return ''
    out = ''
    for i, nama, batas in GERBANG:
        v = _angka(layers[i].get('score'))
        if v is None:
            continue
        ok = v >= batas
        col = 'green' if ok else 'red'
        out += (f'<div style="border: 1px solid var(--border); border-radius: 8px; padding: 3px 6px; background: var(--bg-alt);">'
                f'<div style="{MONO} font-size: 8px; color: var(--text-muted);">{nama}</div>'
                f'<div style="font-size: 9px; font-weight: 700; color: {c(col)};">{"Lolos" if ok else "Gagal"}</div></div>')
    return (f'<div style="{MONO} font-size: 8px; letter-spacing: 0.08em; color: var(--text-muted); margin-top: 2px;">GERBANG MINIMUM</div>'
            f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0px,1fr)); gap: 4px; margin-top: 3px;">{out}</div>') if out else ''


def b_resources(b):
    cols = b.get('columns', 3)
    return (f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0px, 1fr)); column-gap: 16px; margin-top: 6px;">' +
            ''.join(f'<div style="display: grid; grid-template-columns: 18px minmax(0px, 1fr) auto; gap: 6px; align-items: baseline; padding: 3px 0px; border-bottom: 1px solid var(--border);">'
                    f'<span style="{MONO} font-size: 8.5px; color: var(--success-solid);">{i + 1:02d}</span><span data-ed="1" style="font-size: 9.5px; color: var(--white);">{n}</span>'
                    f'<span data-ed="1" style="{MONO} font-size: 8.5px; color: var(--text-muted);">{d}</span></div>' for i, (n, d) in enumerate(b['items'])) + '</div>')


def b_spacer(b):
    return f'<div style="height: {b.get("h", 10)}px;"></div>'


def b_html(b):
    return b['html']


def b_image(b):
    """Embedded image (data URI or URL) on a light plate, with caption. src, caption, plate ('light'|'none'), h (max height px)"""
    plate = b.get('plate', 'light')
    bgc = '#ffffff' if plate == 'light' else 'transparent'
    mh = f' max-height: {b["h"]}px;' if b.get('h') else ''
    cap = f'<div data-ed="1" style="font-size: 9px; color: var(--text-muted); margin-top: 4px; line-height: 1.45;">{b["caption"]}</div>' if b.get('caption') else ''
    return (f'<div style="margin-top: {b.get("mt", 6)}px;"><div style="background: {bgc}; border-radius: 8px; padding: {6 if plate == "light" else 0}px; overflow: hidden;">'
            f'<img src="{b["src"]}" alt="{b.get("alt", "")}" style="display: block; width: 100%;{mh} object-fit: contain;"></div>{cap}</div>')


def b_donut(b):
    """Donut chart with legend. slices [{label, value, color, display}], center_top, center_bottom, size"""
    import math
    S = b.get('size', 150)
    r_out, r_in = S / 2 - 2, S / 2 - 2 - b.get('thick', 26)
    cx = cy = S / 2
    total = sum(x['value'] for x in b['slices'])
    a = -math.pi / 2
    paths = ''
    for x in b['slices']:
        frac = x['value'] / total
        a2 = a + frac * 2 * math.pi
        large = 1 if frac > 0.5 else 0
        gap = 0.012 if frac > 0.02 else 0.004
        s0, s1 = a + gap / 2, a2 - gap / 2
        p = [(cx + r_out * math.cos(s0), cy + r_out * math.sin(s0)), (cx + r_out * math.cos(s1), cy + r_out * math.sin(s1)),
             (cx + r_in * math.cos(s1), cy + r_in * math.sin(s1)), (cx + r_in * math.cos(s0), cy + r_in * math.sin(s0))]
        paths += (f'<path d="M{p[0][0]:.2f},{p[0][1]:.2f} A{r_out},{r_out} 0 {large} 1 {p[1][0]:.2f},{p[1][1]:.2f} L{p[2][0]:.2f},{p[2][1]:.2f} '
                  f'A{r_in},{r_in} 0 {large} 0 {p[3][0]:.2f},{p[3][1]:.2f} Z" fill="{c(x.get("color", "green"))}"><title>{x["label"]}: {x.get("display", "")}</title></path>')
        a = a2
    # teks tengah dikecilkan bila lebih lebar dari ±80% lubang (huruf mono ±0,6 em)
    top = re.sub(r'<[^>]+>|&[a-z]+;', 'x', str(b.get('center_top', '')))
    fs = min(b.get('center_size', 18), round(r_in * 2 * 0.8 / max(len(top) * 0.6, 1), 1))
    ctr = (f'<text x="{cx}" y="{cy - 2}" text-anchor="middle" fill="var(--white)" font-size="{fs}" font-weight="700" font-family="var(--font-mono)">{b.get("center_top", "")}</text>'
           f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" fill="var(--text-muted)" font-size="8.5" font-family="var(--font-mono)">{b.get("center_bottom", "")}</text>')
    svg = f'<svg viewBox="0 0 {S} {S}" width="{S}" height="{S}" role="img" aria-label="{b.get("aria", "Donut")}" style="display: block; flex: 0 0 auto;">{paths}{ctr}</svg>'
    leg = ''.join(f'<div style="display: grid; grid-template-columns: 10px minmax(0px,1fr) auto auto; gap: 7px; align-items: center; padding: 2.5px 0px; border-bottom: 1px solid var(--border); font-size: 9.5px;">'
                  f'<span style="width: 9px; height: 9px; border-radius: 2px; background: {c(x.get("color", "green"))};"></span>'
                  f'<span data-ed="1" style="color: {"var(--white)" if x.get("bold") else "var(--text-body)"};{" font-weight: 700;" if x.get("bold") else ""}">{x["label"]}</span>'
                  f'<span data-ed="1" style="{MONO} color: var(--text-body); text-align: right;">{x.get("display", "")}</span>'
                  f'<span data-ed="1" style="{MONO} color: var(--text-muted); text-align: right; min-width: 40px;">{x.get("share", "")}</span></div>' for x in b['slices'])
    return f'<div style="display: flex; gap: 16px; align-items: center;">{svg}<div style="flex: 1 1 auto; min-width: 0px;">{leg}</div></div>'


def b_steps(b):
    """Horizontal process steps. items [{title, text, color}] with arrows between."""
    n = len(b['items'])
    cols = ' 14px '.join(['minmax(0px,1fr)'] * n)
    out = f'<div style="display: grid; grid-template-columns: {cols}; align-items: stretch; margin-top: {b.get("mt", 4)}px;">'
    for i, it in enumerate(b['items']):
        col = c(it.get('color', 'green'))
        out += (f'<div style="background: var(--bg-alt); border: 1px solid var(--border); border-top: 3px solid {col}; border-radius: 6px; padding: 7px 8px;">'
                f'<div style="{MONO} font-size: 8.5px; color: {col}; letter-spacing: 0.06em;">LANGKAH {i + 1}</div>'
                f'<div data-ed="1" style="font-weight: 700; color: var(--white); font-size: 10.5px; line-height: 1.3; margin-top: 2px;">{it["title"]}</div>'
                f'<div data-ed="1" style="font-size: 9.5px; color: var(--text-body); line-height: 1.45; margin-top: 3px;">{it["text"]}</div></div>')
        if i < n - 1:
            out += '<div style="display: flex; align-items: center; justify-content: center; color: var(--text-muted); font-size: 12px;">→</div>'
    return out + '</div>'


BLOCKS = {k[2:]: v for k, v in globals().items() if k.startswith('b_') and callable(v)}


def blocks(lst):
    out = ''
    for b in lst:
        t = b.get('type')
        if t not in BLOCKS:
            raise ValueError(f'Tipe blok tidak dikenal: {t}')
        out += BLOCKS[t](b)
    return out


# ------------------------------------------------------------------ pages
def header(meta, n, subtitle, logo):
    return ('<div style="position: absolute; top: 0px; left: 0px; right: 0px; height: 3px; background: var(--accent-rule);"></div>'
            '<header style="display: flex; justify-content: space-between; align-items: flex-end; padding-bottom: 14px; border-bottom: 1px solid var(--border);">'
            '<div class="sc-host-x" style="display: contents;"><span style="display: inline-flex; align-items: center; gap: 7.8px;">'
            f'<img src="{logo}" alt="" style="height: 26px; display: block;">'
            '<span style="font-family: var(--font-sans); font-weight: 800; letter-spacing: 0.02em; color: var(--white); font-size: 13px; line-height: 1;">SHARIACRYPTO<span style="color: var(--success-solid);">.</span></span></span></div>'
            f'<div style="text-align: right; {MONO} font-size: 9px; letter-spacing: 0.06em; color: var(--text-muted); line-height: 1.7;">'
            f'<div data-ed="1" style="color: var(--white); font-weight: 500;">{meta["header_line"]}</div>'
            f'<div data-ed="1">Halaman {n} — {subtitle}</div></div></header>')


def footer(disc, n, total):
    return ('<footer style="position: absolute; left: 44px; right: 44px; bottom: 22px; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; padding-top: 10px; border-top: 1px solid var(--border);">'
            f'<p style="margin: 0px; max-width: 540px; font-size: 9px; line-height: 1.55; color: var(--text-muted);">{disc}</p>'
            f'<div style="{MONO} font-size: 9px; color: var(--text-muted); text-align: right; line-height: 1.7;"><span data-pgnum="1">{n} / {total}</span><br>shariacrypto.id</div></footer>')


def coin_logo(x):
    """Logo koin di hal. 1: exec.logo (data URI / <svg>) atau exec.logo_file (file teks berisi data URI, hasil rn_logo.py).
    Tanpa logo -> lencana ticker sederhana bila exec.ticker diisi."""
    src = x.get('logo', '')
    if not src and x.get('logo_file'):
        src = open(x['logo_file'], encoding='utf-8').read().strip()
    alt = f'Logo {re.sub("<[^>]+>", "", x["name"])}'
    if src.startswith('<svg'):
        return f'<span role="img" aria-label="{alt}" style="display: inline-flex; width: 34px; height: 34px; flex: none;">{src}</span>'
    if src:
        return f'<img src="{src}" alt="{alt}" style="width: 34px; height: 34px; border-radius: 50%; object-fit: contain; flex: none; display: block;">'
    if x.get('ticker'):
        return (f'<span aria-label="{alt}" style="display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; '
                f'background: var(--surface-card); border: 1px solid var(--border-strong); {MONO} font-size: 10px; font-weight: 700; color: var(--white); flex: none;">{x["ticker"][:4]}</span>')
    return ''


def coin_name(x):
    lg = coin_logo(x)
    if not lg:
        return x['name']
    return f'<span style="display: inline-flex; align-items: center; gap: 10px;">{lg}{x["name"]}</span>'


def exec_page(x, meta, logo, total, disc):
    hdr = ('<div style="position: absolute; top: 0px; left: 0px; right: 0px; height: 3px; background: var(--accent-rule);"></div>'
           '<header style="display: flex; justify-content: space-between; align-items: flex-end; padding-bottom: 12px; border-bottom: 1px solid var(--border);">'
           '<div class="sc-host-x" style="display: contents;"><span style="display: inline-flex; align-items: center; gap: 7.8px;">'
           f'<img src="{logo}" alt="" style="height: 26px; display: block;">'
           '<span style="font-family: var(--font-sans); font-weight: 800; letter-spacing: 0.02em; color: var(--white); font-size: 13px; line-height: 1;">SHARIACRYPTO<span style="color: var(--success-solid);">.</span></span></span></div>'
           f'<div style="text-align: right; {MONO} font-size: 9px; letter-spacing: 0.06em; color: var(--text-muted); line-height: 1.7;">'
           '<div style="color: var(--white); font-weight: 500;">CRYPTO RESEARCH NOTE</div>'
           f'<div data-ed="1">{x["dateline"]}</div><div data-ed="1">Shariacrypto Research · Bagian 1 — Executive Summary</div></div></header>')
    t = x['target']
    hero = ('<section style="display: grid; grid-template-columns: 1fr 232px; gap: 22px; align-items: stretch; padding: 16px 0px 14px;">'
            '<div style="display: flex; flex-direction: column; justify-content: flex-end;">'
            f'<div data-ed="1" style="font-weight: 800; font-size: 30px; letter-spacing: -0.02em; color: var(--white); line-height: 1.1;">{coin_name(x)}</div>'
            f'<div data-ed="1" style="{MONO} font-size: 10.5px; letter-spacing: 0.06em; color: var(--text-muted); margin-top: 5px;">{x["subtitle"]}</div>'
            '<div data-chips="1" style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px;">' +
            ''.join(chip(ch['t'], ch.get('c', 'muted'), ch.get('dot', False)) for ch in x['chips']) + '</div></div>'
            '<div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 12px 14px; text-align: right;">'
            f'<div style="{MONO} font-size: 9px; letter-spacing: 0.08em; color: var(--text-muted);">{t.get("label", "TARGET 12 BULAN · SKENARIO DASAR")}</div>'
            f'<div data-ed="1" style="{MONO} font-variant-numeric: tabular-nums; font-weight: 700; font-size: {t.get("size", 38)}px; line-height: 1.1; letter-spacing: -0.02em; margin-top: 2px; background: var(--gradient-focal); -webkit-background-clip: text; background-clip: text; color: transparent;">{t["price"]}</div>'
            f'<div data-ed="1" style="{MONO} font-size: 10.5px; color: {c(t.get("ret_color", "green"))};">{t["ret"]}</div>'
            f'<div style="display: flex; justify-content: space-between; gap: 8px; {MONO} font-size: 9px; color: var(--text-muted); margin-top: 7px; padding-top: 7px; border-top: 1px solid var(--border);">'
            f'<span data-ed="1">{t["bear"]}</span><span data-ed="1" style="color: var(--white);">{t["mid"]}</span><span data-ed="1">{t["bull"]}</span></div></div></section>')
    body = ('<div style="display: grid; grid-template-columns: minmax(0px, 1fr) 232px; gap: 22px;">'
            f'<div style="display: flex; flex-direction: column;">{blocks(x["left"])}</div>'
            f'<aside style="display: flex; flex-direction: column;">{blocks(x["right"])}</aside></div>')
    return (f'<div data-page="1" data-screen-label="01 Executive summary" style="{PAGE_STYLE}">' + hdr + hero + body + footer(disc, 1, total) + '</div>')


def build(content, shell):
    m = re.search(r'(<script type="application/json" id="doc-data">)(.*?)(</script>)', shell, re.S)
    if not m:
        raise SystemExit('Shell tidak berisi <script id="doc-data">')
    doc = json.loads(m.group(2))
    logo = re.search(r'<img src="(data:image/png;base64,[^"]+)"', doc['html']).group(1)
    meta = content['meta']
    discs = content['disclaimers']
    pages = content['pages']
    total = len(pages)
    html = '<div data-main="1" style="display: flex; flex-direction: column; align-items: center; gap: 32px; padding: 32px 16px 64px;">'
    for i, p in enumerate(pages, 1):
        disc = discs[p.get('disclaimer', 'A')]
        if 'exec' in p:
            html += exec_page(p['exec'], meta, logo, total, disc)
        else:
            html += (f'<div data-page="{i}" data-screen-label="{i:02d} {p.get("label", "")}" style="{PAGE_STYLE}">'
                     + header(meta, i, p['subtitle'], logo) + blocks(p['blocks']) + footer(disc, i, total) + '</div>')
    html += '</div>'
    doc['html'] = ikonkan(html)
    doc['title'] = meta['title']
    doc['css'] = doc.get('css', '')
    data = json.dumps(doc, ensure_ascii=False).replace('<', '\\u003c')
    out = shell[:m.start(2)] + data + shell[m.end(2):]
    out = re.sub(r'<title>.*?</title>', '<title>' + meta['title'].replace('&', '&amp;') + '</title>', out, count=1)
    return out


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    content = json.load(open(sys.argv[1], encoding='utf-8'))
    shell = open(sys.argv[2], encoding='utf-8').read()
    out = build(content, shell)
    open(sys.argv[3], 'w', encoding='utf-8').write(out)
    print('OK', sys.argv[3], len(out), 'bytes,', len(content['pages']), 'halaman')
