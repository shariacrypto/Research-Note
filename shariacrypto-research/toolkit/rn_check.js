// Usage: node rn_check.js note.html [outdir]
// Prints per-page free space (px) before the footer; negative = overflow. Also lists text wider than its column. Saves page PNGs to outdir if given.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const file = path.resolve(process.argv[2]); const outdir = process.argv[3];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1.5 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + file); await p.waitForTimeout(1500);
  const r = await p.$$eval('[data-page]', ps => ps.map(pg => {
    const f = pg.querySelector(':scope > footer'); const lim = f.getBoundingClientRect().top; let max = 0;
    pg.querySelectorAll('*').forEach(e => { if (f.contains(e) || e.closest('[data-ui]')) return; const r = e.getBoundingClientRect(); if (r.height > 0 && r.bottom > max) max = r.bottom; });
    // teks yang meluber keluar kolomnya (mis. angka panjang di kolom sempit)
    const lebar = [];
    pg.querySelectorAll('[data-ed]').forEach(e => { if (getComputedStyle(e).display === 'inline') return; if (e.scrollWidth > e.clientWidth + 1) lebar.push(e.textContent.trim().slice(0, 40)); });
    return { page: pg.getAttribute('data-screen-label'), free: Math.round(lim - max), lebar };
  }));
  let bad = 0;
  const rows = await p.$$eval('[data-chips]', cs => cs.map(el => new Set([...el.children].map(ch => Math.round(ch.getBoundingClientRect().top))).size));
  if (rows.length && rows[0] > 2) { bad++; console.log(`CHIP      hal. 1: ${rows[0]} baris (maks. 2) — pendekkan teks chip`); }
  for (const x of r) { const st = x.free < 0 ? 'OVERFLOW' : (x.free > 80 ? 'KOSONG' : 'OK'); if (st !== 'OK') bad++; console.log(`${st.padEnd(9)} ${x.page}: sisa ${x.free}px`); if (x.lebar.length) { bad++; console.log(`  MELUBER  ${x.lebar.length} teks lebih lebar dari kolomnya: ${x.lebar.slice(0, 4).map(t => JSON.stringify(t)).join(', ')}`); } }
  if (errs.length) console.log('JS errors:', errs);
  if (outdir) { const pages = await p.$$('[data-page]'); for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: path.join(outdir, `hal${i + 1}.png`) }); }
  console.log(bad ? `${bad} halaman perlu disesuaikan (target sisa 0–80px).` : 'Semua halaman OK.');
  await b.close();
})();
