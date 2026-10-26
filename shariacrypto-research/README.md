# Shariacrypto Research — paket awal Claude Code

Paket ini memindahkan run Research Note dari Cowork ke **Claude Code** dengan lapisan data API gratis, uji data otomatis, dan pustaka grafik. Versi aturan: **Metodologi v3.1 + PANDUAN v3.2** (`docs/PANDUAN.md`).

## Isi paket

| Folder/berkas | Isi |
|---|---|
| `CLAUDE.md` | Ringkasan aturan proyek, dibaca Claude otomatis setiap sesi |
| `.claude/skills/research-note/SKILL.md` | Prompt run langkah demi langkah (`/research-note APT`) |
| `docs/PANDUAN.md` | PANDUAN v3.2 lengkap (v3.1 + amandemen 26 Okt 2026). `PANDUAN_v3.1.md` disimpan sebagai arsip |
| `scdata/` | Pengambil data: DefiLlama, CoinGecko, CoinMarketCap, Binance, Dex Screener, GitHub + uji identitas suplai, rekonsiliasi konflik, beta, snapshot CSV |
| `charts/` | 8 jenis grafik note APT (indeks vs BTC, unlock, fee per aplikasi, valuasi, kipas skenario, proyeksi batas suplai, titik impas, peta suplai) |
| `toolkit/` | `rn_build.py`, `rn_check.js`, `rn_shell.html`, `rn_logo.py`, contoh konten (versi terbaru) |
| `assets/` | Config per aset (`APT.json`, `_TEMPLATE.json`) dan font Inter (lisensi OFL) |
| `examples/APT_2026-10-22/` | Note APT terakhir: generator, konten, snapshot, arsip, grafik |
| `tests/test_offline.py` | Uji tanpa internet (API dipalsukan) |

## Langkah 1 — Siapkan kunci API (gratis, ±10 menit)
1. **CoinGecko Demo**: daftar di coingecko.com → Developer Dashboard → buat Demo API key.
2. **CoinMarketCap Basic**: daftar di pro.coinmarketcap.com → salin API key.
3. **GitHub token** (opsional, disarankan): GitHub → Settings → Developer settings → Fine-grained token, tanpa izin tambahan (hanya baca repo publik).
4. DefiLlama, Binance, dan Dex Screener tidak butuh kunci.

Salin `.env.example` menjadi `.env` dan isi kuncinya **hanya di komputer sendiri**. `.env` tidak boleh di-commit (sudah ada di `.gitignore`).

## Langkah 2 — Buat repo GitHub privat
1. Buat repo **privat** baru, mis. `shariacrypto-research`.
2. Ekstrak zip ini, lalu unggah seluruh isinya (termasuk folder tersembunyi `.claude/` dan berkas `.gitignore`). Cara termudah lewat terminal:
   ```bash
   cd shariacrypto-research
   git init && git add . && git commit -m "paket awal"
   git branch -M main
   git remote add origin https://github.com/<akun>/shariacrypto-research.git
   git push -u origin main
   ```

## Langkah 3 — Coba di komputer (opsional, disarankan sekali)
Butuh Python 3.10+, Node 18+, dan langganan Claude Pro/Max.
```bash
# pasang Claude Code (macOS/Linux; Windows PowerShell: irm https://claude.ai/install.ps1 | iex)
curl -fsSL https://claude.ai/install.sh | bash

pip install -r requirements.txt
npm install && npx playwright install chromium

python tests/test_offline.py                 # harus mencetak "[scdata] APT: ... metrik"
python -m scdata.fetch assets/APT.json       # ambil data sungguhan
python -m charts.render charts/examples_APT.json /tmp/cek   # 8 grafik contoh
```
Buka `data/out/APT_<tgl>/checks.md` dan `fetch_log.txt`: semua sumber inti harus `OK`.

## Langkah 4 — Pindahkan ke cloud (Claude Code di web)
1. Buka claude.ai/code, hubungkan akun GitHub, pilih repo `shariacrypto-research`.
2. Buat **environment** untuk repo ini:
   - **Akses jaringan: Custom**, izinkan domain berikut:
     `api.llama.fi`, `coins.llama.fi`, `stablecoins.llama.fi`, `api.coingecko.com`, `pro-api.coinmarketcap.com`, `fapi.binance.com`, `api.binance.com`, `data-api.binance.vision`, `api.dexscreener.com`, `api.github.com`, `raw.githubusercontent.com`, `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org`, `cdn.playwright.dev`, `playwright.download.prss.microsoft.com`, serta situs riset yang sering dipakai (mis. `defillama.com`, `coingecko.com`, `coinmarketcap.com`, `messari.io`, `blockworks.co`, explorer rantai yang dianalisis).
   - **Variabel lingkungan**: `COINGECKO_API_KEY`, `CMC_API_KEY`, `GITHUB_TOKEN`.
   - **Skrip setup**: `pip install -r requirements.txt && npm install && npx playwright install chromium`
3. Hubungkan konektor **Google Drive** dan **Google Docs** di pengaturan konektor claude.ai, lalu di sesi Claude Code jalankan `/mcp` untuk memastikan keduanya aktif.

Catatan: nama menu di claude.ai bisa berubah. Bila ada yang berbeda, tanyakan di sesi Claude Code: "bagaimana mengatur network allowlist dan env var untuk environment ini?"

## Langkah 5 — Uji coba manual (wajib sebelum dijadwalkan)
Di sesi Claude Code pada repo ini, ketik:
```
/research-note APT uji coba, jangan unggah ke Drive dan jangan tulis log
```
Periksa: `fetch_log.txt` (sumber gagal?), `checks.md` (uji suplai LULUS?), grafik, dan hasil `rn_check.js`. **Pengambil data di paket ini belum pernah dijalankan ke API sungguhan** (lingkungan pembuatannya memblokir API); yang sudah diuji adalah logika parsing dengan data palsu, grafik, dan toolkit. Bila ada endpoint yang berubah format, minta Claude memperbaikinya di sesi ini, lalu commit.

## Langkah 6 — Jadwalkan (Routine)
Buat routine di claude.ai/code (atau ketik `/schedule` di sesi):
- **Jadwal**: Senin, Rabu, Jumat 11.15 WIB = 04.15 UTC → cron `15 4 * * 1,3,5`
- **Repo & environment**: yang dibuat di Langkah 4
- **Prompt**:
  > Jalankan skill /research-note sesuai CLAUDE.md dan docs/PANDUAN.md. Pilih aset dengan aturan antrean §7. Jangan mengirim email dan jangan sertakan saran konten media sosial. Akhiri dengan pesan singkat: aset, empat label + sikap, link note dan Doc arsip, hasil uji data, pertanyaan untuk Komite.

Pemakaian routine dihitung dari kuota langganan Claude yang sama.

## Menambah aset baru
Salin `assets/_TEMPLATE.json` → `assets/<TICKER>.json`. Yang wajib diisi dengan teliti: `suplai_manual.komponen` (dari sumber primer; tandai komponen yang merupakan bagian dari komponen lain) dan `pembanding` (wajib pemimpin kategori). Skill akan membuatkan config bila belum ada, tetapi periksa hasilnya.

## Masalah umum
- **Binance HTTP 451/403**: Binance memblokir sebagian IP cloud AS. Data Binance opsional; beta otomatis memakai CoinGecko.
- **CoinGecko 429**: batas paket Demo tercapai; `scdata` menunggu dan mengulang otomatis. Jalankan dengan `--no-peers` untuk mengurangi panggilan.
- **GitHub kosong**: `stats/contributors` kadang perlu beberapa detik untuk dihitung; jalankan ulang.
- **DefiLlama slug salah**: cek di defillama.com/chain/<nama> dan defillama.com/protocol/<slug>, perbaiki config.
- **Grafik memakai font lain**: pastikan `assets/fonts/*.otf` ikut ter-commit.
