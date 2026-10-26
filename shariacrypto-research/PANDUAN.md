# PANDUAN — Shariacrypto Research Note Harian

Dokumen ini adalah aturan baku untuk menyusun **Shariacrypto Research Note** (PDF siap sebar, 9–11 halaman A4). Contoh acuan kualitas, gaya, dan bahasa: **Research Note Ethereum (Rev. 9 Okt 2026)** — isinya ada di `contoh_ETH.json`.

> **Rev. 9 Okt 2026:** (1) wajib ada **Glosarium** di halaman terakhir; (2) bahasa Indonesia yang mudah dipahami penutur asli dan tidak terasa "ditulis AI" (§4 Bahasa); (3) blok baru `image`, `donut`, `steps` untuk visual yang menjelaskan konsep (contoh: tokenisasi di Ethereum dengan data rwa.xyz, hal. 4 contoh ETH).

## 1. Berkas toolkit

| File | Fungsi |
|---|---|
| `rn_build.py` | `python3 rn_build.py content.json rn_shell.html note.html` → membangun halaman note dari JSON |
| `rn_shell.html` | Cangkang: CSS brand, font, logo, editor (Edit isi / Edit template / Simpan versi / Unduh HTML / Simpan PDF) |
| `rn_check.js` | `node rn_check.js note.html outdir` → cek tiap halaman: sisa ruang 0–80px = OK; negatif = OVERFLOW; >80px = KOSONG. Juga menyimpan PNG tiap halaman |
| `contoh_ETH.json` | Contoh konten lengkap 11 halaman (Rev. 9 Okt). **Salin strukturnya, ganti isinya** |

Playwright & Chromium sudah terpasang di lingkungan (jalankan `node` dengan `NODE_PATH=$(npm root -g)`).

## 2. Bahan masukan

> **Rev. 5 Okt 2026:** laporan FA terpisah **tidak lagi wajib**. Bila ada laporan FA yang cocok, pakai sebagai titik awal (lalu cek silang angkanya). Bila tidak ada, jalankan **FA-lite (§9)** di dalam run RN. Uji 5 Okt 2026: note GEOD dibuat penuh tanpa FA; note DOGE menunjukkan laporan FA bisa memuat angka keliru (suplai 171,82 M vs 156,19 M yang benar), jadi riset ulang tetap diperlukan.

1. **Laporan FA harian (opsional)** di Google Drive folder "Shariacrypto FA Harian" (id `1BCfoNo4L-AOArf0AOMKgyfeKF4Lm1PrQ`): Google Doc berjudul `FA_<TICKER>_<YYYY-MM-DD> — Laporan Analisis Fundamental ...`. Ini sumber utama: skor composite, skor & verdict syariah 4 lapis, tokenomics, on-chain, makro, valuasi & peers, katalis, risiko, positioning, sumber.
2. **Log** `FA_Log_Shariacrypto.txt` dan `RN_Log_Shariacrypto.txt` (selalu pakai file berjudul persis itu yang paling baru; id di prompt lama bisa usang).
3. **Riset tambahan via web** untuk melengkapi yang belum ada di laporan FA: perubahan kepemilikan ±3/6/12 bulan, arus ETF/treasury, revenue 12 bulan & struktur biaya (DefiLlama/Token Terminal), data katalis terukur, berita 7 hari terakhir. Jangan mengarang angka. Yang tidak tersedia ditulis "N/A"; hasil hitungan sendiri diberi label "(est.)" atau "ESTIMASI".

## 3. Struktur wajib (6 bagian)

| Hal. | Isi | Catatan |
|---|---|---|
| 1 | **1. Executive Summary** — header aset, chip (Signal · composite, Syariah verdict skor, Skew/R/R, Hold/Conviction), target base 12 bln + bear/expected/bull; 1.1 Investment thesis (CORE / WHY NOW / VARIANT); 1.2 Katalis singkat C1–C3 (ringkasan dari detail, dengan peluang & timing); 1.3 Positioning verdict (tabel skenario); 1.4 Prediksi harga 2030 (bila relevan); aside: Key metrics, Target dua lensa, satu blok data terbaru (mis. arus ETF) | Tidak ada blok risiko di hal. 1 |
| 2–3 | **2. Business Highlight** — 2.1 Distribusi holder + perubahan kepemilikan (kini, ±3, ±6, ±12 bulan, status berwarna); 2.2 Institutional backing (+ konsentrasi); 2.3 Bagaimana protokol menghasilkan uang (aliran pendapatan 12 bln, ke mana, driver); 2.4 Struktur biaya & income statement (Sankey arus pendapatan + bar pembanding bila ada pos yang jauh lebih besar, mis. issuance) + pesan utama | Sesuaikan dengan model bisnis aset (lihat §6) |
| 4–7 | **3. Detail Katalis** — ringkasan 3 kartu, **3.1 visual penjelas katalis utama** (alur `steps` + grafik data `donut`/`bars`/`image` dari sumber primer, mis. rwa.xyz untuk tokenisasi), lalu C1, C2, C3 masing-masing kartu detail, ditutup 3.2 Pohon probabilitas skenario + jadwal titik uji | Satu katalis besar per halaman bila perlu |
| 7 | **4. Valuasi vs Peer/Benchmark** — tabel peers, 3 catatan benchmark (mahal/murah/kesimpulan), 4.1 Implied re-rating (minimal dua lensa) + cara baca + heatmap sensitivitas, 4.2 Skenario jangka panjang / prediksi 2030 dengan rumus & asumsi terbuka | |
| 8 | **5. Yang Bisa Mematahkan Tesis** — R1–R3 kartu detail + kotak Positioning verdict (upside tertimbang, downside tertimbang, expected price, R/R) | |
| 10 | **6. Sharia Note** (skor & 4 layer, catatan risiko, status per aktivitas spot/staking/lending), 6.1 Dampak katalis & risiko terhadap status syariah (tabel), 6.2 Dasbor pemantauan (10–11 indikator: kini, target/batas waspada, terkait C/R) | Disclaimer "B" |
| 11 | **7. Sumber** (paragraf + 9–12 key resources) dan **8. Glosarium** (dua tabel ISTILAH · ARTI SINGKAT, 25–30 istilah, urut sesuai kemunculan, ditutup catatan satuan jt/M/T, (est.), N/A) | Disclaimer "B" |

Jumlah halaman boleh 9–11; yang penting **setiap halaman terisi (sisa 0–80px), tidak ada overflow**.

## 4. Aturan isi (preferensi pemilik — wajib)

**Katalis (C1–C3)** — setiap katalis memakai baris: MEKANISME · DAMPAK TERUKUR · INDIKATOR PANTAU · TRIGGER & TIMING · SUMBER IDE · PROBABILITY & CONFIDENCE.
- C1 = katalis paling berdampak ("paling gong"), C2 & C3 sekunder. Pilih katalis yang spesifik untuk aset itu (mis. ETH: tokenisasi, deflasi, ETF/treasury).
- **Mekanisme** dijelaskan sebagai rantai sebab-akibat yang jelas (bagaimana nilai mengalir ke token), termasuk "kebocoran"/hal yang membuatnya gagal.
- **Dampak terukur BUKAN "+x%"**. Tulis metrik (KPI) yang bisa diukur, nilai kini, skenario 12 bln (berlabel ESTIMASI), dan **cara mengukurnya** (sumber data). Bila diterjemahkan ke harga, pakai rumus eksplisit (mis. harga implisit = rasio × metrik ÷ suplai) dalam blok `formula`.
- **Probability** didefinisikan sebagai kejadian yang bisa diverifikasi (metrik X mencapai Y pada tanggal Z), plus Confidence (Low/Medium/High) dan alasannya.
- Indikator pantau: daftar konkret dengan ambang/alarm.

**Risiko (R1–R3)** — baris: MEKANISME · DAMPAK TERUKUR · INDIKATOR PANTAU · PROBABILITY. Tanpa "expected loss = prob × −x%".

**Positioning verdict / R/R** — diturunkan dari probabilitas skenario, bukan dari dampak "+x%":
- Bull = kombinasi katalis utama terwujud (mis. P(C1) × P(C3), sebutkan asumsi independensi).
- Bear = risiko thesis-killer (R1) — probabilitas kejadian harga menyentuh target bear dalam 12 bln.
- Base = sisa (100% − bull − bear).
- E[harga] = Σ prob × target. Upside tertimbang = Σ prob × (target − harga kini) untuk bull & base; downside tertimbang = prob bear × (harga kini − target bear). **R/R = upside ÷ downside.**
- Label: R/R ≥ 2 → "SKEW POSITIF"; 1–2 → "SEIMBANG / FAIRLY POSITIONED"; < 1 → "CONDONG KE RISIKO". Tampilkan di hal. 1, 3.2, 4.1, dan kotak akhir Bagian 5 — angkanya harus sama di semua tempat.
- Target bull/base/bear diambil dari laporan FA; boleh disesuaikan bila data baru menuntut, dengan alasan tertulis.

**Valuasi** — peers tidak hanya yang market cap-nya mirip; **wajib** sertakan pemimpin kategori (mis. BTC untuk aset moneter, ETH/SOL untuk L1, HYPE untuk perp DEX). Pakai fee/revenue aktual 12 bulan (bukan annualisasi 1 hari). Minimal dua lensa re-rating; tunjukkan "seberapa berat" asumsi tiap target.

**Prediksi jangka panjang (2030)** — selalu dengan rumus & asumsi terbuka (ukuran pasar × porsi × rasio ÷ suplai), labelnya "bukan target 12 bulan".

**Syariah** — salin skor & verdict 4-Layer dari laporan FA (atau hitung dengan FA-lite §9.4 dan beri label "(est.)") (L1 0–30, L2 0–30, L3 0–10, L4 0–30; gate L1<12, L3<4, L4<12; ≥80 SHARIA ALIGNED, 60–79 MUSHTABIH, 40–59 HIGH CONCERN, <40 NON-COMPLIANT). Tambahkan catatan risiko yang muncul dari katalis (mis. katalis RWA berbasis bunga menekan L3) dan status per aktivitas (spot/staking/lending/perp). Selalu "bukan fatwa".

**Bahasa (target pembaca: orang Indonesia awam hingga menengah)**
- Tulis seperti analis Indonesia menjelaskan ke klien: kalimat pendek, aktif, satu gagasan per kalimat. Hindari terjemahan kata per kata dari bahasa Inggris.
- Pakai kata Indonesia yang umum bila ada: "pendapatan" (bukan revenue), "dibakar" (bukan burn), "ETH baru/pencetakan" (bukan issuance), "pemegang" (bukan holder), "peluang" (bukan probability), "keyakinan" (bukan confidence), "pemicu & waktu" (bukan trigger & timing), "pemusatan" (bukan konsentrasi/centralization), "harga rata-rata" untuk E[harga], "batas waspada" untuk alarm.
- Istilah kripto yang memang lazim (staking, stablecoin, fee, gas, ETF, DEX, L1/L2, market cap) boleh dipakai, tetapi **wajib masuk glosarium**. Istilah framework milik Shariacrypto (Business Highlight, Positioning verdict, Bull/Base/Bear, Composite, nama verdict syariah) tetap dipakai dan juga masuk glosarium.
- Label kecil di halaman memakai bahasa Indonesia: METRIK UTAMA, TESIS INVESTASI (INTI · KENAPA SEKARANG · YANG TERLEWAT), DUKUNGAN INSTITUSI, MEKANISME · DAMPAK TERUKUR · INDIKATOR PANTAU · PEMICU & WAKTU · SUMBER IDE · PELUANG & KEYAKINAN.
- Hindari gaya "AI": em-dash berlebihan, pola "bukan X, melainkan Y", kalimat titik-dua-lalu-kejutan, kata klise ("perlu dicatat", "menariknya", "lanskap", "krusial"), dan tanda kutip untuk istilah buatan.
- Saat menjelaskan konsep baru (mis. tokenisasi), mulai dari definisi satu kalimat dengan contoh nyata, baru masuk ke angka.

**Lain-lain**
- Angka format Indonesia ($2.687,85; 1,89×; "jt" = juta, "M" = miliar, "T" = triliun). Grafik dari sumber berbahasa Inggris (mis. "B" = billion) diberi keterangan satuan di caption.
- Grafik/gambar dari pihak ketiga selalu diberi caption sumber + tanggal data; angka yang dibaca dari grafik (bukan tabel) diberi label "perkiraan dibaca dari grafik (est.)".
- Jangan sertakan saran konten/thread media sosial. Jangan kirim lewat Gmail.
- Setiap angka penting punya tanggal data; sumber dicantumkan di Bagian 7.

## 5. Komponen JSON (`rn_build.py`)

Struktur atas: `{"meta": {"title", "header_line"}, "disclaimers": {"A","B","EXEC"}, "pages": [...]}`.
Halaman 1: `{"disclaimer": "EXEC", "exec": {"dateline","name","subtitle","chips":[{t,c,dot}],"target":{price,ret,bear,mid,bull},"left":[blok],"right":[blok]}}`.
Halaman lain: `{"label","subtitle","disclaimer":"A"|"B","blocks":[blok]}`.

Warna: `green, gold, orange, red, info, muted, white, warning, body, blue, darkred`. Teks boleh HTML inline (`<strong style="color: var(--white);">`, `<br>`, `&amp;`, `&lt;`).

| `type` | Field utama | Dipakai untuk |
|---|---|---|
| `bigsec` | num, title, mt | Judul bagian besar (2, 3, 4…) |
| `sub` | num, title, right, mt | Sub-bagian (2.1, 4.2…) |
| `h9` | num, title, right, mt, mb | Judul kecil di hal. 1 |
| `text` | html, muted, size, mt, mb | Paragraf |
| `note` / `formula` | html | Catatan kecil / rumus bergaris putus |
| `ul` / `ol` | items[] | Daftar |
| `table` | cols (CSS grid), header[], rows[][], hl[], align[], size, mt | Tabel. Sel: teks, `{"n": nilai, "c": warna, "b": true, "s": sub}`, `{"t": label, "s": sub}`, `{"dot": warna, "t": teks}` |
| `mtab` | header, rows, cols, hl | Tabel mini di dalam kartu |
| `card` | label, label_color, accent, blocks[], mt | Kartu |
| `grid` | cols, gap, align, mt, items[] (blok atau list blok) | Tata letak kolom |
| `kv` | rows [[kunci, nilai, warna]] | Key metrics |
| `thesis` | rows [[label, teks]] | CORE/WHY NOW/VARIANT |
| `srows` | rows [{tag, title, body, right, tagc, rcolor}] | Katalis singkat |
| `scen` | label, right, rows [{name,color,prob,target,ret,basis}], note | Verdict skenario hal. 1 |
| `tiles` | items [{label, value, color, sub}] | Ubin angka (prediksi 2030) |
| `tgt` | heads[], rows [{name,color,price,ret,vals[]}] | Target dua lensa |
| `bars` | rows [{label,value,color,display}], max, label_width | Bar pembanding skala linear |
| `split` | segments [{label,value,color,label_color}] (color "dim" = abu) | Bar 100% dua bagian |
| `sankey` | source {label, display}, flows [{label,value,display,color}] | Arus pendapatan |
| `heat` | row_labels, col_labels, values[][], thresholds [bawah, atas], corner, prefix (default "$"), decimals (default 0; pakai 2–3 untuk harga < $10) | Heatmap sensitivitas (merah < bawah ≤ kuning < atas ≤ hijau) |
| `tree` | nodes [{title, sub, color, prob}] | Pohon probabilitas |
| `timeline` | rows [[tanggal, peristiwa, tag]] | Kalender katalis |
| `dcard` | tag, title, subtitle, pills [{t,c}], accent, rows [{label, blocks[]}], title_size, mt | Kartu detail katalis/risiko |
| `stats` | verdict, color, items [{label,value,color,sub}], note | Kotak positioning verdict |
| `sharia` | score, verdict, verdict_color, summary, layers [{label,name,icon,icon_color,text,score,pct}], after[] | Sharia note |
| `resources` | items [[nama, domain]], columns | Key resources |
| `spacer` | h | Jarak manual |
| `image` | src (data URI JPEG/PNG, kompres ≤100 KB), alt, caption, plate (`light` = alas putih untuk screenshot grafik), h, mt | Grafik/screenshot sumber primer |
| `donut` | slices [{label, value, color, display, share, bold}], center_top, center_bottom, size, thick | Porsi/komposisi (mis. pangsa jaringan) dengan legenda |
| `steps` | items [{title, text, color}] (3–5 langkah) | Alur proses sederhana (mis. cara kerja tokenisasi) |

## 6. Menyesuaikan dengan jenis aset

- **L1 dengan fee & burn (ETH, BNB, SOL, TRX):** seperti contoh ETH.
- **Aset moneter PoW (BTC, DOGE, LTC, XMR, ZEC):** 2.3 = aliran pendapatan miner (subsidi blok vs fee); 2.4 Sankey "biaya keamanan" (subsidi + fee → miner) dengan bar pembanding fee vs subsidi; katalis tipikal: adopsi pembayaran/ETF, perubahan suplai/halving, upgrade teknis.
- **Protokol dengan revenue ke holder (HYPE, dll.):** 2.3 per lini produk; Sankey revenue → (holder via buyback/burn, treasury, biaya operasional/insentif); lensa valuasi utama P/S & P/E holder.
- **Token tanpa revenue on-chain:** tulis terus terang di 2.3; ganti Sankey dengan bar struktur suplai/emisi dan alokasi; lensa valuasi alternatif (MC/aktivitas, MC/TVL, peers kategori).
- Status holder (2.1) memakai kategori relevan untuk aset tersebut (bursa, ETF, treasury, tim/VC, unlock, whale, staking, dsb).

## 7. Alur kerja run harian (ringkas)

1. Tentukan aset (urutan prioritas; selalu lewati ticker yang sudah punya note ≤30 hari di `RN_Log_Shariacrypto.txt`):
   a. Laporan FA hari ini (Framework v3) yang belum punya note.
   b. Bila tidak ada: **skrining hidden gem** (§9.1) dan pilih kandidat dengan valuasi ÷ pendapatan holder paling menarik yang lolos filter.
   c. Bila skrining tidak menghasilkan kandidat layak: aset market cap terbesar (CMC/CoinGecko) yang belum punya note; lewati stablecoin, token wrapped/bridged, dan liquid staking derivative.
2. Bahan: baca laporan FA bila ada; bila tidak, jalankan FA-lite (§9). Dalam kedua kasus, lakukan riset tambahan untuk data yang dibutuhkan struktur note.
3. Tentukan C1–C3 dan R1–R3 dengan framework di §4; hitung skenario, E[harga], R/R; periksa aritmetika dengan Python.
4. Tulis `content_<TICKER>.json` (mulai dari salinan `contoh_ETH.json`), bangun, lalu jalankan `rn_check.js`. Ulangi (pangkas/tambah isi, ubah `mt`, pindahkan blok antarhalaman) sampai semua halaman OK. Lihat PNG minimal hal. 1, 3, dan 7.
5. Terbitkan note sebagai artifact baru (capabilities: `{"artifact": {}, "downloads": true}`), judul `Shariacrypto Research Note — <Nama> (<TICKER>) — <tgl>`.
6. Simpan arsip di Drive (lihat §8).

## 8. Arsip & log di Drive

- Buat Google Doc di folder "Shariacrypto FA Harian": `RN_<TICKER>_<YYYY-MM-DD> — Shariacrypto Research Note <Nama>` berisi: link artifact, verdict & R/R, target & probabilitas skenario, C1–C3 & R1–R3 (satu baris masing-masing), prediksi 2030, dasbor pemantauan, dan catatan asumsi/run. Bila memakai FA-lite, sertakan juga tabel skor 6 dimensi (beserta sub-skor) dan skor syariah per lapis dengan alasan singkat: Doc ini sekaligus menjadi arsip FA aset tersebut.
- Log: `RN_Log_Shariacrypto.txt` (buat bila belum ada). Konektor Drive tidak bisa mengedit file: buat ulang log berisi isi lama + baris baru, lalu ganti judul log lama menjadi `RN_Log_Shariacrypto_USANG_sebelum_<tanggal>.txt`. Format baris: `YYYY-MM-DD | TICKER | Nama | R/R | verdict syariah | link artifact | link Doc`.

## 9. FA-lite — skoring di dalam run RN (tanpa laporan FA)

Dipakai bila tidak ada laporan FA yang cocok, atau bila laporan FA lebih tua dari 14 hari. Semua skor hasil FA-lite diberi label **"(est.)"** di chip hal. 1, kotak Sharia, dan Doc arsip; disclaimer EXEC menyebut "dibuat tanpa laporan FA".

### 9.1 Skrining hidden gem (pemilihan aset tanpa FA)
1. Buka `defillama.com/holders-revenue` (WebFetch berhasil untuk halaman situs; API DefiLlama/CoinGecko/Blockchair diblokir robots.txt). Ambil 25–40 protokol teratas.
2. Untuk tiap kandidat, buka `defillama.com/protocol/<slug>`: MC, FDV, holders revenue 30d / 7d / 1y, revenue kuartalan.
3. Hitung **MC ÷ holders revenue** dan **FDV ÷ holders revenue**, masing-masing atas TTM aktual dan run-rate 7 hari (×52). Pakai yang paling konservatif sebagai angka utama.
4. **Cek lonjakan sesaat:** bila revenue 30 hari jauh di atas rata-rata kuartalan atau run-rate 7 hari, anggap 30 hari itu anomali (contoh 5 Okt 2026: AERO tampak 4,8× atas 30 hari, padahal ±17× atas run-rate 7 hari).
5. **Filter keluar:** volume 24 jam < $1 jt; revenue dari launchpad memecoin, lotre/gamified mining, atau perp/lending sebagai bisnis inti (rapuh dan biasanya gagal gate syariah); protokol < 6 bulan; ticker yang sudah punya note ≤30 hari.
6. Pilih satu; tuliskan tabel skrining singkat (kandidat, rasio, alasan ditolak) di Doc arsip.

### 9.2 Data dasar & cek silang (wajib)
- Harga/MC/suplai: CoinGecko **dan** CoinMarketCap. Bila suplai beredar berbeda > 3%, pakai yang konsisten dengan explorer/rich list/BitInfoCharts dan catat selisihnya.
- Revenue: DefiLlama (TTM aktual + kuartalan); bila tidak ada, Token Terminal atau laporan resmi proyek. Jangan menganualisasi 1 hari.
- Vesting/unlock: Tokenomist / Tokenradar; hitung unlock 12 bulan ke depan dalam token, % suplai beredar, dan nilai USD.
- Makro: pakai bagian makro laporan FA terbaru di folder bila ≤ 7 hari; bila tidak, riset (BTC, ATH, BTC.D, total MC, US10Y, DXY, M2 global, jadwal FOMC).

### 9.3 Composite 6 dimensi (bobot sama dengan template FA Framework v3)
Skor tiap dimensi = rata-rata tertimbang sub-skor 1–10:

| Dimensi (bobot) | Sub-kriteria (bobot) |
|---|---|
| Tokenomics (20%) | Scarcity 20 · Emission 20 · Distribution 15 · Vesting 15 · Utility 20 · Burn 10 |
| On-Chain / Jaringan (20%) | Network growth 25 · On-chain valuation (MVRV dll.) 25 · Exchange flow 20 · Dev 15 · Decentralization 15 |
| Macro (15%) | Cycle 25 · Liquidity 25 · Regulation 20 · Institutional 15 · De-dollarization 15 |
| Valuation (15%) | FDV/MC 25 · P/S vs peers 25 · Upside/Downside 30 · Liquidity 20 |
| Risk — kualitas, terbalik (10%) | 10 − rata-rata (severity × probability ÷ 10) untuk 8 kategori: smart contract/protokol, regulasi, likuiditas, tim/key person, konsentrasi, makro/sistemik, kompetisi, bridge |
| Sharia (20%) | skor 4-Layer ÷ 10 |

Signal: ≥8 STRONG BUY · ≥7 BUY · ≥5,5 NEUTRAL · ≥4 CAUTION · <4 AVOID. Hitung dengan Python; cantumkan sub-skor di Doc arsip.
Red flag checklist (Ya/Tidak): tim anonim · tanpa audit · tim/VC > 30% · FDV/MC > 5× · umur < 6 bulan · copycat · tanpa utilitas · janji imbal hasil · founder dumping.

### 9.4 Sharia 4-Layer (total 100)
- **L1 Infrastruktur (0–30):** riba/staking berbunga/lending di level protokol, premine & alokasi, open-source, apa yang ditampung jaringan.
- **L2 Utilitas token (0–30):** gas/fee, alat bayar layanan, upah kerja (ju'alah), staking (asal imbal hasilnya), governance. L2 bukan gate.
- **L3 Paparan pendapatan non-halal (0–10):** porsi revenue dari riba/judi/sektor haram (ambang SAC/AAOIFI ≤ 5%), value-source test, kebutuhan tathir.
- **L4 Usage (0–30):** 4a maysir/zero-sum (porsi derivatif vs spot); 4b dominasi manfaat riil. Spekulasi atau volatilitas BUKAN kriteria haram.
- **Gate:** NON-COMPLIANT bila L1 < 12, L3 < 4, atau L4 < 12. Verdict: ≥80 SHARIA ALIGNED · 60–79 MUSHTABIH · 40–59 HIGH CONCERN · < 40 NON-COMPLIANT.
- Cross-reference Sharlife / PIF / IFG (tulis N/A bila belum ada kajian). Sebutkan hal yang perlu diverifikasi untuk menaikkan/menurunkan skor. Selalu "bukan fatwa".

## 10. Pelajaran teknis dari run sebelumnya
- WebFetch ke halaman situs DefiLlama/CoinGecko/CMC berhasil; endpoint API (`api.coingecko.com`, `api.llama.fi`, `api.blockchair.com`) diblokir — jangan buang token mencobanya.
- Ringkasan WebFetch bisa salah label (mis. "1 thn +61,8%" padahal −63,7%): cek silang angka penting dengan sumber kedua.
- Heatmap harga < $10: isi `"decimals": 3` di blok `heat`.
- Sankey dengan aliran < 1% tidak terlihat dan labelnya bertumpuk: keluarkan dari Sankey, sebutkan di note.
- Klaim di media sosial (mis. "whale beli X") tanpa dompet/sumber yang bisa dicek tidak dipakai sebagai data.
