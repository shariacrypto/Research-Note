# Shariacrypto Research — panduan proyek untuk Claude

Repo ini menghasilkan **Shariacrypto Research Note** (Analisis Perdana, Bahasa Indonesia) dengan **Metodologi v3.1 + PANDUAN v3.2**. Aturan lengkap: `docs/PANDUAN.md` — **wajib dibaca utuh sebelum run note** (skill `/research-note` melakukannya). File ini hanya ringkasan agar sesi biasa (mengedit kode) tetap hemat token.

## Peta repo
- `scdata/` — pengambil data API gratis (DefiLlama, CoinGecko, CMC, Binance, Dex Screener, GitHub). `python -m scdata.fetch assets/<T>.json` → `data/out/<T>_<tgl>/` (snapshot CSV, `summary.json`, `checks.md`, `series/`, `raw/`).
- `charts/` — 8 jenis grafik gaya Shariacrypto dari spec JSON. `python -m charts.render <spec.json> <outdir>`.
- `toolkit/` — `rn_build.py` (JSON → HTML), `rn_check.js` (cek halaman, Playwright), `rn_shell.html`, `rn_logo.py`, contoh konten.
- `assets/<T>.json` — config per aset (id API, komponen suplai dari sumber primer, klasifikasi syariah per kategori aplikasi, pembanding). `assets/fonts/` — Inter (OFL).
- `examples/APT_2026-10-22/` — note lengkap terakhir (16 halaman, 8 grafik) sebagai acuan pola.
- `.claude/skills/research-note/SKILL.md` — prompt run langkah demi langkah.

## Aturan emas (ringkas; detail di PANDUAN)
1. **Data dulu, tulisan kemudian.** Jalankan `scdata.fetch`; baca `summary.json` + `checks.md`, jangan membaca `raw/` (boros token).
2. **Hierarki sumber**: primer (explorer, dokumen/proposal resmi) > API agregator > riset pihak ketiga > media. Media tidak dipakai untuk angka suplai/unlock/fee.
3. **Konflik > 20%** (suplai > 3%, volume > 50%) wajib direkonsiliasi dan dijelaskan; jangan memilih angka konservatif begitu saja.
4. **Uji identitas suplai** harus LULUS sebelum menulis bagian suplai/unlock. Komponen yang merupakan bagian komponen lain tidak dijumlah dua kali.
5. **Klaim sebab-akibat didekomposisi** dengan angka (mis. burn = transaksi × gas/transaksi × harga gas).
6. **Label dari skor dibulatkan 1 desimal**; syariah dibulatkan tanpa desimal.
7. **Grafik 4–8**, judul = kesimpulan, sumber + tanggal data di tiap grafik, PNG ≤ 100 KB.
8. **Riset mandiri**: tidak ada bagian "perbandingan dengan Messari"; temuan pihak ketiga yang terverifikasi diolah sebagai analisis sendiri dengan sumber disebut.
9. Tampilan: warna hanya untuk makna, tanpa emoji, angka format Indonesia (1.234,5; juta/miliar), angka dan satuan tidak dipisah.
10. Jangan mengirim email; jangan menyertakan saran konten media sosial; jangan mengubah baris lama log; jangan commit `.env`.

## Google Drive
Folder kerja: `1BCfoNo4L-AOArf0AOMKgyfeKF4Lm1PrQ` ("Shariacrypto FA Harian"). Konektor Drive tidak bisa mengedit file: buat ulang file + ganti judul file lama `_USANG_sebelum_<YYYY-MM-DD>`.

## Perintah cepat
- Uji tanpa internet: `python tests/test_offline.py`
- Contoh grafik: `python -m charts.render charts/examples_APT.json /tmp/cek`
- Bangun note: `python toolkit/rn_build.py content.json toolkit/rn_shell.html note.html && node toolkit/rn_check.js note.html shots`
