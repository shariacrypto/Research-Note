# PANDUAN v3.2 — Shariacrypto Research Note (Metodologi v3.1)

Dokumen ini adalah aturan baku untuk menyusun **Shariacrypto Research Note** (PDF siap sebar, 12–16 halaman A4). Sumber aturan penilaian adalah **Metodologi Riset Shariacrypto v3.1** (dokumen pemilik, 20 Okt 2026, https://claude.ai/code/artifact/522f6811-02d4-4303-8da9-f98db8f061fa). PANDUAN ini menerjemahkannya ke langkah kerja run. Bila PANDUAN dan dokumen Metodologi berbeda, dokumen Metodologi yang berlaku. Contoh tata letak dan gaya: `toolkit/contoh_ETH.json`; contoh note lengkap dengan grafik: `examples/APT_2026-10-22/`.

> **Rev. 26 Okt 2026 — PANDUAN v3.2 (disetujui pemilik).** Disusun dari evaluasi note APT 22 Okt 2026 (lima kesalahan data: unlock 54,5 juta padahal ±21 juta/th, kunci 210 juta dihitung dua kali, nomor proposal tertukar, klaim sebab kenaikan burn tanpa dekomposisi, kritik metrik pihak ketiga yang ternyata keliru). Perubahan:
> 1. **Lapisan data API** (`scdata/`): angka inti diambil lewat API, bukan ringkasan halaman web. Snapshot dibuat otomatis (§8.1).
> 2. **Hierarki sumber** dan **rekonsiliasi wajib** untuk selisih > 20% (§4A.1–4A.2).
> 3. **Uji identitas suplai otomatis** sebelum menulis bagian suplai/unlock (§4A.3).
> 4. **Dekomposisi** untuk setiap klaim sebab-akibat (§4A.4).
> 5. **Riset pihak ketiga** dicek ulang dan sponsornya dicatat (§4A.5).
> 6. **Porsi fee per aplikasi** di rantai L1/L2 diukur dan menjadi masukan L3/L4 syariah (§4A.6).
> 7. **Grafik wajib 4–8** dengan judul berupa kesimpulan (§5.2).
> 8. **Label dari skor dibulatkan 1 desimal** (§4A.7) — tidak ada lagi skor "6,99".
> 9. **Analisis Khusus** maks. 2 halaman untuk temuan yang tidak masuk template (§3); batas halaman 12–16.

> **Rev. 20 Okt 2026 — Metodologi v3.1.** Perubahan besar:
> 1. **Skor fundamental 4 dimensi** (Tokenomics 30 · Jaringan & Bisnis 30 · Nilai ke Pemegang 25 · Risiko 15) dengan **rubrik kuantitatif** (§9.3). Makro dan Valuasi tidak lagi masuk skor.
> 2. **Skenario dijangkarkan ke Pandangan Pasar Bulanan** dan beta terhadap BTC (§4 Skenario). Bull = P(C1)×P(C3) dan bear = peluang "menyentuh" **tidak dipakai lagi**.
> 3. **Rantai Nilai ke Pemegang** dan **Hasil Bersih Pemegang** wajib (§4).
> 4. **Label bahasa Indonesia** dan **matriks sikap** (§4 Label). Status syariah: Sesuai Syariah ≥80 · Halal Bersyarat 60–79 · Banyak Catatan 40–59 · Tidak Sesuai Syariah <40 atau gagal gerbang (Rev. 20 Okt, ditetapkan pemilik).
> 5. **Jalur Syariah / Jalur Umum** dan **tier ukuran aset**; token yang tidak lolos syariah dan token kecil tetap boleh dianalisis penuh (§7).
> 6. **Kuota 3 note per minggu** (minimal 2 Jalur Syariah), aturan antrean tetap, skor prioritas 40/25/20/15 (§7).
> 7. Katalis disebut **Pendorong (P1–P3)**; Risiko tetap R1–R3.
> 8. Pengungkapan kepemilikan, snapshot data, log peluang, serta tinjauan, penyesuaian komite, dan veto pemilik (§8, §11).
>
> `contoh_ETH.json` sudah memakai label baru, tetapi **angkanya masih dari metodologi lama** (peluang 20/45/35, skor 6,6, singkatan jt/M). Salin strukturnya, jangan angkanya, dan ikuti aturan angka di §4.
>
> Riwayat sebelumnya: Rev. 19 Okt (bagian 3 Analisis On-Chain; footer shariacrypto.id) · Rev. 13 Okt (chip hal. 1, ilustrasi sederhana, logo koin, Riwayat draf) · Rev. 9 Okt (glosarium, bahasa, blok image/donut/steps).

## 1. Berkas toolkit

| File | Fungsi |
|---|---|
| `scdata/` | `python -m scdata.fetch assets/<TICKER>.json` → snapshot CSV, `summary.json`, `checks.md`, deret waktu untuk grafik (§4A, §8.1) |
| `charts/` | `python -m charts.render charts_<TICKER>.json <outdir>` → PNG ≤ 100 KB gaya Shariacrypto (§5.2) |
| `rn_build.py` | `python3 rn_build.py content.json rn_shell.html note.html` → membangun halaman note dari JSON |
| `rn_shell.html` | Cangkang: CSS brand, font, logo, editor (Baca / Edit isi / Edit template / ↶ ↷ / **Riwayat** / Simpan versi / Unduh HTML / Simpan PDF) |
| `rn_logo.py` | `python3 rn_logo.py TICKER --tw <jalur Trust Wallet>` → logo koin dari sumber terbuka sebagai data URI |
| `rn_check.js` | `node rn_check.js note.html outdir` → cek tiap halaman (sisa 0–80px = OK; negatif = OVERFLOW; >80px = KOSONG), jumlah baris chip hal. 1 (maks. 2), teks yang MELUBER dari kolomnya, simpan PNG |
| `contoh_ETH.json` | Contoh konten 11 halaman dengan label v3.1 (angka dari metodologi lama). Belum memuat bagian on-chain: saat menyalin, sisipkan halaman on-chain dan naikkan nomor bagian berikutnya |
| `contoh_onchain_BTC.json` | Contoh 3 halaman **Analisis On-Chain** (Bitcoin, 19 Okt 2026). Sisipkan setelah Business Highlight |

Semua berkas toolkit ada di `toolkit/`. Playwright: `npm install` lalu `npx playwright install chromium` sekali saat setup (lihat README).

## 2. Bahan masukan

1. **Pandangan Pasar Bulanan** (wajib, §4 Skenario): Google Doc di folder "Shariacrypto FA Harian" (id `1BCfoNo4L-AOArf0AOMKgyfeKF4Lm1PrQ`) berjudul diawali `Pandangan_Pasar_<YYYY-MM>`. Pakai bulan berjalan; bila belum ada, bulan terakhir yang tersedia.
2. **Laporan FA (opsional)**: Google Doc `FA_<TICKER>_<YYYY-MM-DD> …` ≤14 hari. Dipakai sebagai bahan, tetapi skornya **dihitung ulang** dengan rubrik v3.1 (§9.3); angka penting dicek silang.
3. **Log**: `RN_Log_Shariacrypto.txt`, `RN_Peluang_Shariacrypto.txt`, dan (bila ada) Doc `RN_Permintaan_Shariacrypto` — selalu file berjudul persis itu yang terbaru.
4. **Pengungkapan kepemilikan**: Doc `Pengungkapan_Kepemilikan_Shariacrypto` bila ada. Bila tidak ada, pakai daftar baku di §8.
5. **Data API** (wajib, §4A): jalankan `scdata.fetch`; baca `summary.json` dan `checks.md`, **bukan** `raw/`.
6. **Riset web**: data struktur note, pendorong terukur, berita 7 hari. Jangan mengarang angka; yang tidak tersedia ditulis "N/A"; hitungan sendiri diberi label "(est.)". Sumber per kebutuhan ada di §9.2.

## 3. Struktur wajib (7 bagian + sumber & glosarium)

| Hal. | Isi | Catatan |
|---|---|---|
| 1 | **1. Ringkasan** — header aset + logo; subjudul memuat **ticker · tier ukuran · jalur · modul sektor · peringkat** (Jalur Umum ditambah "· tidak untuk portofolio syariah"); dateline memuat tanggal data dan **"Metodologi v3.1"**; **4 chip dalam maks. 2 baris** (§4 Label); kotak target 12 bulan (Skenario Dasar + Pesimis / Perkiraan / Optimis); 1.1 Tesis investasi (**INTI · KENAPA SEKARANG · BISA SALAH BILA**); 1.2 Pendorong singkat P1–P3; 1.3 Ringkasan skenario (tabel); 1.4 Gambaran jangka panjang 2030 (bila relevan); aside: Metrik utama (baris terakhir **Fundamental x,x · Label**; Aset Kecil/Mikro juga memuat volume harian, FDV/MC, unlock 12 bln), target dua cara hitung, satu blok data terbaru | Pengungkapan kepemilikan masuk disclaimer EXEC |
| 2–3 | **2. Business Highlight** — 2.1 Distribusi pemegang + perubahan kepemilikan; 2.2 Dukungan institusi; 2.3 Bagaimana protokol menghasilkan uang; 2.4 Struktur biaya + **Rantai Nilai ke Pemegang** (tabel 5 tingkat, §4) | Sesuaikan dengan modul sektor (§6) |
| 4–6 | **3. Analisis On-Chain** (§4 On-chain) | Contoh `contoh_onchain_BTC.json` |
| 7–10 | **4. Detail Pendorong** — ringkasan 3 kartu, 4.1 visual penjelas pendorong utama, P1–P3 kartu detail, 4.2 pohon skenario + jadwal titik uji | |
| 10–11 | **5. Valuasi vs Pembanding** — tabel pembanding (wajib pemimpin kategori), **cek kelipatan target** (§4 Skenario), 5.1 dua lensa + heatmap, 5.2 Gambaran jangka panjang 2030; paragraf **"Mengapa pasar keliru menilai"** bila Harga Perkiraan > +30% | |
| 11–12 | **6. Yang Bisa Mematahkan Tesis** — R1–R3 kartu detail + kotak Ringkasan Skenario (Potensi Naik, Potensi Turun, Harga Perkiraan, Rasio Untung-Rugi) + kalimat **Sikap** dengan keyakinan dan zona harga | |
| 13 | **7. Catatan Syariah** — status, 4 lapis, **status 6 aktivitas**, pembanding eksternal (+ paragraf selisih bila > 20 poin), tathir; 7.1 Dampak pendorong & risiko terhadap status syariah; 7.2 Dasbor Pantauan (6–10 indikator, termasuk 2–3 on-chain) | Disclaimer "B" |
| + | **Analisis Khusus** (opsional, maks. 2 halaman, v3.2) — temuan yang paling menarik untuk publik tetapi tidak muat di template (mis. batas suplai APT, titik impas deflasi). Ditempatkan di bagian yang paling relevan (biasanya Bagian 4) sebagai sub-bagian bernomor; wajib memakai minimal 1 grafik | Tidak boleh mengulang isi bagian lain |
| 14 | **8. Sumber** dan **9. Glosarium** (25–30 istilah, urut kemunculan, ditutup catatan satuan) | Disclaimer "B" |

Setiap halaman terisi (sisa 0–80px), tanpa overflow.

## 4. Aturan isi (wajib)

**Pendorong (P1–P3)** — setiap pendorong memakai baris: MEKANISME · DAMPAK TERUKUR · INDIKATOR PANTAU · PEMICU & WAKTU · SUMBER IDE · PELUANG & KEYAKINAN.
- P1 = pendorong paling berdampak; P2 & P3 sekunder; spesifik untuk aset itu.
- **Mekanisme**: rantai sebab-akibat bagaimana nilai mengalir ke token, termasuk kebocorannya.
- **Dampak terukur dibuka dengan "Ilustrasi sederhana"**:
  1. Blok `text` diawali `<strong>Ilustrasi sederhana:</strong>` — 2–3 kalimat dengan satuan sehari-hari, membandingkan kebutuhan pendorong dengan sesuatu yang dikenal pembaca. Hindari rasio berantai.
  2. Blok `bars` 2–4 baris pada skala yang sama.
  3. Bila perlu skala kedua, satu kalimat + `bars` kedua.
  4. Baru kemudian `mtab` UKURAN · KINI · 12 BLN LAGI* · SUMBER DATA, dan rumus di `note`/`formula`.
  Contoh JSON (note Bitcoin Rev. 12 Okt):
  ```json
  {"type":"text","html":"<strong style=\"color: var(--white);\">Ilustrasi sederhana:</strong> setiap hari jaringan “mencetak” ±450 BTC baru. Supaya P1 tercapai, institusi cukup menyerap ±625 BTC per hari selama setahun. Pada September mereka menyerap ±1.180 per hari, jadi lajunya sudah hampir dua kali yang dibutuhkan."},
  {"type":"bars","label_width":230,"max":1300,"rows":[{"label":"BTC baru ditambang per hari","value":450,"color":"orange","display":"±450 BTC"},{"label":"Kebutuhan P1 per hari","value":625,"color":"gold","display":"±625 BTC"},{"label":"Dibeli ETF + Strategy (Sep 2026)","value":1180,"color":"green","display":"±1.180 BTC"}]}
  ```
- **Dampak terukur bukan "+x%"**: metrik, nilai kini, skenario 12 bln (ESTIMASI), dan cara mengukurnya. Terjemahan ke harga memakai rumus eksplisit di `formula`.
- **Peluang** = kejadian yang bisa diverifikasi (metrik X mencapai Y pada tanggal Z), **kelipatan 5%**, plus keyakinan Tinggi/Sedang/Rendah dan alasannya.
- Pendorong dan risiko **tidak lagi dikalikan** untuk membentuk skenario. Keduanya masuk ke skenario hanya lewat **alfa** yang ditautkan (lihat Skenario).

**Risiko (R1–R3)** — baris: MEKANISME · DAMPAK TERUKUR · INDIKATOR PANTAU · PELUANG (kelipatan 5%, dengan tenggat). Tanpa "expected loss".

**Skenario 12 bulan (Metodologi §6)**
1. Ambil **Pandangan Pasar Bulanan**: target BTC Optimis/Dasar/Pesimis dan peluangnya. Peluang skenario token **sama** dengan peluang BTC.
   - Bila belum ada Doc Pandangan Pasar sama sekali: pakai skenario BTC dari Research Note BTC terbaru, dibulatkan ke kelipatan 5% (per 8 Okt 2026: Optimis $130.000 · 20%, Dasar $100.000 · 55%, Pesimis $60.000 · 25%), beri label **"Pandangan Pasar sementara — belum ditetapkan Komite"** di catatan skenario dan di catatan run, lalu tetap selesaikan note.
2. **Beta** = kemiringan regresi return mingguan token terhadap BTC selama 52 minggu, dibatasi 0,5–2,5. Coba halaman data historis (mis. CoinGecko `/historical_data`, Yahoo Finance `<TICKER>-USD/history`) lewat WebFetch. Bila data tidak bisa diambil, atau umur token < 52 minggu, pakai **beta asumsi per modul** dan tandai "(beta asumsi)": Uang/penyimpan nilai selain BTC 1,2 · Token Bursa & CeFi 1,2 · L1 1,3 · Jaringan Pembayaran 1,3 · DEX, Perpetual DEX, Lending/CDP, RWA, Stablecoin & Dolar Sintetis, Staking Cair 1,5 · L2/Rollup 1,6 · Infrastruktur/AI/DePIN 1,7 · Gaming/NFT 1,8 · Meme, Launchpad 2,0. BTC sendiri beta 1,0.
3. **Target** tiap skenario: `harga kini × (1 + beta × return BTC skenario + alfa)`. Alfa (poin persentase) wajib ditautkan ke P atau R tertentu dan dijelaskan satu kalimat. Alfa > 25 poin di satu skenario hanya boleh bila sudah disetujui Komite; run tanpa persetujuan memakai batas 25 poin dan mencatatnya.
4. **Cek kelipatan**: market cap tersirat tiap target ÷ Nilai Diterima Pemegang (atau metrik utama modul), dibandingkan dengan pemimpin kategori. Bila melebihi pemimpin kategori, tulis alasan satu paragraf di Bagian 5.
5. **Skenario Khusus**: kejadian khusus token dengan peluang ≥10% dan dampak ≥40% (delisting besar, depeg, eksploitasi) menjadi skenario keempat; peluangnya diambil proporsional dari tiga skenario lain.
6. **Semua skenario = harga akhir 12 bulan**, bukan harga yang sempat disentuh. Peluang menyentuh suatu level boleh ditulis di dasbor sebagai risiko perjalanan harga, tidak masuk hitungan.
7. Hitung dengan Python: **Harga Perkiraan** = Σ peluang × target · **Potensi Naik** = Σ peluang × kenaikan (skenario di atas harga kini) · **Potensi Turun** = Σ peluang × penurunan (skenario di bawah harga kini) · **Rasio Untung-Rugi** = Potensi Naik ÷ Potensi Turun. Angka identik di semua tempat.
8. **Uji kewajaran**: Harga Perkiraan > +30% → paragraf "Mengapa pasar keliru menilai" di Bagian 5.

**Rantai Nilai ke Pemegang (Metodologi §5)** — tabel di 2.4 (12 bulan terakhir, dolar):
1. Fee kotor · 2. Pendapatan protokol · 3. Holders revenue (DefiLlama) · 4. **Nilai Diterima Pemegang** = distribusi tunai + buyback-burn bersih (buyback dikurangi token yang diterbitkan ulang), diverifikasi dari sumber primer (dashboard/laporan resmi protokol, Dune, explorer) · 5. **Hasil Bersih Pemegang** = Nilai Diterima − (emisi ke pihak lain + unlock orang dalam 12 bln ke depan + hibah) × harga kini.
- Emisi yang hanya dibagi ke pemegang yang sama (mis. staking) tidak dihitung sebagai dilusi dan tidak dihitung sebagai Nilai Diterima.
- Kelipatan valuasi utama = market cap ÷ Nilai Diterima Pemegang; market cap ÷ holders revenue hanya pembanding sekunder.
- Bila Nilai Diterima tidak bisa diverifikasi, tulis "N/A — belum terverifikasi", pakai holders revenue dengan label "(proksi, belum terverifikasi)", dan turunkan keyakinan sikap satu tingkat.
- Modul Uang tidak memakai rantai ini; isi 2.3–2.4 dengan biaya keamanan (subsidi + fee → penambang) dan Kekuatan Moneter (§9.3).

**Label (Metodologi §9) — satu-satunya label yang boleh dipakai**

| Sumbu | Ambang → Label | Warna chip |
|---|---|---|
| Fundamental | ≥8,0 Sangat Kuat · 7,0–7,99 Kuat · 5,5–6,99 Cukup · 4,0–5,49 Lemah · <4,0 Sangat Lemah | green · green · warning · orange · red |
| Harga (Rasio Untung-Rugi) | ≥2,0 Harga Murah · 1,0–1,99 Harga Wajar · <1,0 Harga Mahal (selalu "menurut model Shariacrypto") | green · warning · red |
| Syariah | Sesuai Syariah · Halal Bersyarat · Banyak Catatan · Tidak Sesuai Syariah (§9.4) | green · warning · orange · red |
| Aktivitas syariah | Boleh · Bersyarat (sebut syaratnya) · Hindari | — |
| Keyakinan | Keyakinan Tinggi · Keyakinan Sedang · Keyakinan Rendah | — |

**Matriks sikap** (sikap diturunkan otomatis, bukan dipilih):

| Fundamental ↓ / Harga → | Harga Murah | Harga Wajar | Harga Mahal |
|---|---|---|---|
| Sangat Kuat / Kuat | Beli Bertahap | Beli Saat Turun | Tahan |
| Cukup | Beli Saat Turun | Pantau Dulu | Kurangi Bertahap |
| Lemah / Sangat Lemah | Pantau Dulu | Hindari | Hindari |

- Warna sikap: green (Beli Bertahap, Beli Saat Turun) · warning (Tahan, Pantau Dulu) · orange (Kurangi Bertahap) · red (Hindari).
- Aset Jalur Umum tetap memakai hasil matriks, ditambah penanda "tidak untuk portofolio syariah" di subjudul hal. 1 dan di kalimat Sikap Bagian 6.
- Run selalu memakai hasil matriks. Sikap yang berbeda hanya lewat penyesuaian Komite Rating atau veto pemilik setelah run, dan hasil matriks semula tetap dicatat.
- Chip hal. 1, urutan tetap, maks. 2 baris (contoh): `[{t:"Fundamental: Cukup · 6,6", c:"warning", dot:true}, {t:"Harga: Murah · rasio 2,5×", c:"green", dot:true}, {t:"Syariah: Sesuai · 80", c:"green"}, {t:"Beli Saat Turun · keyakinan sedang", c:"green"}]`. Bila lebih dari 2 baris, pendekkan teks, jangan kecilkan huruf.
- Kotak skenario, pohon skenario, kotak Bagian 6: `HARGA MURAH · RASIO ±2,5×`; nama skenario Optimis / Dasar / Pesimis; label angka POTENSI NAIK · POTENSI TURUN · HARGA PERKIRAAN · RASIO UNTUNG-RUGI.
- Kata yang **tidak boleh** muncul di note: Bull/Base/Bear, BUY/NEUTRAL/CAUTION/AVOID, SHARIA ALIGNED/MUSHTABIH/HIGH CONCERN/NON-COMPLIANT (kecuali kutipan pembanding eksternal), composite, positioning verdict, skew, E[harga], katalis C1–C3.

**Analisis On-Chain (Rev. 19 Okt) — Bagian 3, 3 halaman**
Tujuannya menjawab satu pertanyaan: *siapa yang membeli, siapa yang menjual, dan apakah itu mendukung tesis?* Tiap blok ditutup dengan "artinya" dan, bila relevan, dihubungkan ke P/R serta masuk dasbor 3.8 / 7.2.

| Blok | Status | Isi minimum | Sumber yang terbukti bisa diakses |
|---|---|---|---|
| 3.1 Ringkasan sinyal | Wajib | 6 baris: sinyal (Positif/Netral/Campuran/Waspada/Lemah, dot berwarna) · angka kunci · artinya + kesimpulan 1–2 kalimat ke R/R | Turunan blok lain |
| 3.2 Peta pemegang entitas | Wajib | `donut` entitas (ETF, perusahaan, pemerintah, bursa, tim/VC/unlock, kontrak staking/bridge, sisa) + tabel perubahan bertanggal; sebaran saldo alamat bila ada | Media (ETF/treasury), BitcoinTreasuries, Tokenomist, BitInfoCharts distribution; token: halaman holder explorer (Etherscan/Solscan) via WebFetch |
| 3.3 Dompet terbesar & dompet baru | Wajib | 5–8 dompet: label, saldo, perubahan 30 hari, bacaan; dompet tak berlabel ditandai | BitInfoCharts rich list (BTC, DOGE, LTC, dll.), explorer token; berita Arkham/Lookonchain bertanggal |
| 3.4 Perilaku kohort | Opsional bila data hanya arah | Arah per kohort saldo (menambah/datar/menjual) + jumlah dompet whale + holder jangka panjang; boleh hanya arah dengan catatan | Kutipan CryptoQuant/Santiment/Glassnode di media |
| 3.5 Arus bursa | Wajib | Cadangan bursa (sebut penyedia), arus ETF/treasury, permintaan spot vs derivatif, setoran besar dompet tim/VC/unlock ke bursa | CryptoQuant/CoinGlass via media, Farside/SoSoValue |
| 3.6 Umur koin & harga modal | Wajib untuk BTC/ETH; opsional lain | Tangga harga modal (realized price, harga modal ETF, kohort umur) sebagai `bars` relatif terhadap harga dasar; koin tua yang bergerak (ke bursa atau bukan) | Glassnode *The Week On-chain* (gratis, mingguan), berita Arkham |
| 3.7 Kualitas aktivitas | Wajib | Transaksi, fee (median/rata-rata), fee vs subsidi/insentif, alamat aktif dengan definisi sumbernya | BitInfoCharts, DefiLlama (fee/pendapatan), explorer |
| 3.8 Dari on-chain ke tesis | Wajib | 5–6 indikator · kini · target/batas waspada · P/R | — |

Aturan baca (wajib):
- **Alamat ≠ entitas.** Sebut entitas bila labelnya ada; kelompok saldo besar (≥1.000 BTC dsb.) sebagian besar bursa/ETF/kustodian.
- **"Dompet baru yang mengakumulasi"** baru disebut akumulasi bila memenuhi 3 syarat: (1) dana ditarik dari bursa, bukan dipindah dari dompet lain milik bursa/kustodian yang sama; (2) ditahan ≥14 hari tanpa keluar; (3) tidak cocok dengan pola ETF/kustodian (masuk harian sesuai arus dana). Bila belum lolos, tulis "belum terverifikasi". Preseden: "akumulasi whale" Des 2025 ternyata konsolidasi dompet bursa (CryptoQuant).
- **Koin tua bergerak** dibedakan: ke bursa (potensi jual) vs ke alamat baru (biasanya peningkatan keamanan).
- **Jangan bandingkan cadangan bursa antar-penyedia** (CryptoQuant vs CoinGlass memakai daftar alamat berbeda); "alamat aktif" juga beda definisi antar-sumber.
- Klaim media sosial tanpa alamat dompet tidak dipakai. Setiap angka bertanggal.
- Bila suatu blok tidak punya data publik untuk aset tersebut, isi "N/A — tidak tersedia publik" dalam satu baris dan alihkan ruang ke blok lain; jangan mengarang. Untuk altcoin kecil, 3.4 dan 3.6 boleh digabung/dihapus sehingga bagian ini 2 halaman.
- Label entitas dan kohort lengkap butuh layanan berbayar (Arkham, Nansen, Glassnode/CryptoQuant Pro); tulis keterbatasan ini di catatan run, bukan di note untuk customer.

**Logo koin (Rev. 13 Okt)**
- Jalankan `python3 rn_logo.py <TICKER> --tw <jalur>` (jalur Trust Wallet Assets: koin native `blockchains/<chain>/info`, token `blockchains/<chain>/assets/<alamat kontrak/mint>`; cek nama chain di repo trustwallet/assets). Cadangan otomatis: spothq/cryptocurrency-icons (CC0) dan ErikThiart/cryptocurrency-icons (pakai `--sym`).
- **Wajib** lihat PNG/SVG hasilnya: pastikan itu logo aset yang benar (banyak token berbagi ticker). Logo tidak diubah bentuk/warnanya.
- Isi `exec.logo_file: "logo_<TICKER>.txt"` dan `exec.ticker`. Bila semua sumber gagal atau ragu, kosongkan logo: builder menampilkan lencana ticker. Jangan menggambar ulang logo dengan SVG buatan sendiri.
- Cantumkan sumber logo di Bagian 8 (mis. "Logo: Trust Wallet Assets").

**Valuasi** — pembanding wajib menyertakan **pemimpin kategori** modul (§6), bukan hanya market cap serupa. Pakai fee/pendapatan aktual 12 bulan. Minimal dua lensa re-rating dan cek kelipatan target (§4 Skenario). Valuasi **tidak** masuk skor fundamental; hasilnya hanya muncul lewat Rasio Untung-Rugi dan label Harga.

**Gambaran jangka panjang 2030** — rumus & asumsi terbuka (ukuran pasar × porsi × rasio ÷ suplai), selalu berlabel "bukan target 12 bulan". Tidak memengaruhi label apa pun.

**Syariah** — dinilai dengan rubrik §9.4. Ditampilkan sebagai status + keyakinan; angka 0–100 hanya di kotak skor dan Doc arsip, **dibulatkan tanpa desimal**. Selalu "bukan fatwa".

**Bahasa (pembaca: orang Indonesia awam hingga menengah)**
- Tulis seperti analis Indonesia menjelaskan ke klien: kalimat pendek, aktif, satu gagasan per kalimat. Hindari terjemahan kata per kata.
- Pakai kata Indonesia yang umum: pendapatan, dibakar, pemegang, peluang, keyakinan, pemicu & waktu, pemusatan, batas waspada, Pendorong, Harga Perkiraan, Potensi Naik/Turun, Rasio Untung-Rugi, Skenario Optimis/Dasar/Pesimis.
- Sub-skor memakai nama Indonesia: Laju penambahan suplai, Tekanan pelepasan token, Sebaran kepemilikan, Alokasi orang dalam, Kegunaan token, Pertumbuhan penggunaan, Tren pendapatan, Kualitas aktivitas, Aktivitas pengembang, Posisi kompetitif, Tingkat desentralisasi, Mekanisme nilai, Hasil bersih pemegang, Rasio realisasi, Stabilitas pendapatan.
- **Gaya bahasa (keputusan pemilik 20 Okt 2026):** tulis seperti analis menjelaskan ke teman, bukan terjemahan laporan Inggris. Satu ide per kalimat; kalimat pendek. Ganti konsep abstrak dengan gambaran nyata (bukan "dilusi suplai", tetapi "proyek terus mencetak token baru, sehingga keuntungan holder tergerus"). Pakai **"holder"** (variasi: "pemilik token"), bukan "pemegang". Bagian pendapatan yang sampai ke holder lewat buyback, burn, atau bagi fee disebut **"pendapatan holder"** (holders revenue); di kalimat, utamakan kata kerja ("dibagikan ke holder", "sampai ke holder"). Nilai seluruh token ÷ pendapatan holder per tahun disebut **"lama balik modal"** (dalam tahun). Hindari kode internal di teks pembaca (L1–L4, komponen A/B/C/D, rubrik); jelaskan artinya, misalnya "uji unsur judi (maysir)".
- Istilah kripto yang lazim (staking, stablecoin, fee, ETF, DEX, L1/L2, market cap) boleh dipakai, tetapi wajib masuk glosarium. Istilah Inggris lain hanya muncul di glosarium dengan format "Rasio Untung-Rugi (risk/reward, R/R)".
- Hindari gaya "AI": em-dash berlebihan, pola "bukan X, melainkan Y", kalimat titik-dua-lalu-kejutan, kata klise ("perlu dicatat", "menariknya", "lanskap", "krusial").

**Angka**
- Format Indonesia: desimal koma, ribuan titik ($82.900; 3,2×). Tanggal "15 Okt 2026".
- **Angka besar ditulis dengan kata: juta, miliar, triliun** ($1,67 triliun; $270 miliar; $29,2 juta). Singkatan jt/M/T tidak dipakai di note (contoh_ETH masih memakainya — jangan ditiru). Grafik dari sumber berbahasa Inggris diberi keterangan satuan di caption.
- Perkiraan ditandai "(est.)"; angka yang dibaca dari grafik diberi "perkiraan dibaca dari grafik (est.)".
- Skor fundamental ditulis satu desimal (6,6); skor syariah tanpa desimal; peluang kelipatan 5%.

**Lain-lain**
- Grafik/gambar pihak ketiga selalu diberi caption sumber + tanggal data.
- Jangan sertakan saran konten/thread media sosial. Jangan kirim lewat Gmail.
- Setiap angka penting punya tanggal data; sumber dicantumkan di Bagian 8.

## 4A. Integritas data (v3.2, wajib)

**4A.1 Hierarki sumber.** Untuk setiap angka inti, pakai sumber setinggi mungkin:
1. **Primer**: explorer, kontrak, dasbor/dokumen resmi protokol, teks proposal tata kelola (nomor & tanggal dari sumbernya langsung).
2. **Agregator API**: DefiLlama, CoinGecko, CoinMarketCap, Binance, GitHub (lewat `scdata`).
3. **Riset pihak ketiga**: Messari, Blockworks, Everstake, dll. (lihat 4A.5).
4. **Media/berita**: hanya untuk peristiwa dan tanggal, **tidak** untuk angka suplai, unlock, atau fee.
Angka dari tingkat 3–4 yang tidak bisa dicek ke tingkat 1–2 diberi label "(menurut <sumber>)" di note.

**4A.2 Rekonsiliasi wajib.** Bila dua sumber berselisih > 20% (suplai: > 3%; volume: > 50%), `checks.md` menandainya. Run **wajib** mencari penyebab (definisi berbeda, tanggal berbeda, penghitungan ganda) di sumber primer dan menulis satu kalimat penjelasan di Doc arsip. **Dilarang** "menyelesaikan" konflik dengan memilih angka yang paling konservatif tanpa penjelasan.

**4A.3 Uji identitas suplai.** Isi `suplai_manual.komponen` di config dari sumber primer. `scdata` menguji: beredar ≤ total ≤ maks, dan total − beredar = Σ komponen tidak beredar (toleransi 2% total). Komponen yang merupakan **bagian** dari komponen lain (mis. 210 juta APT yang dikunci adalah bagian dari 335 juta yang belum terbuka) ditandai induknya agar tidak dijumlah dua kali. Bagian suplai/unlock dan grafik peta suplai **tidak boleh ditulis** sebelum uji ini LULUS atau selisihnya dijelaskan.

**4A.4 Dekomposisi sebab-akibat.** Klaim "X naik karena Y" wajib dipecah menjadi komponennya dengan angka. Contoh: burn = jumlah transaksi × gas per transaksi × harga gas; tunjukkan perubahan tiap faktor sebelum menyebut penyebab. Bila datanya tidak ada, tulis "kemungkinan" dan sebut faktor yang belum terukur.

**4A.5 Riset pihak ketiga.** Boleh dipakai sebagai bahan dan ide, tetapi: (a) angka kunci dicek ulang ke tingkat 1–2; (b) bila laporan disponsori proyek, catat di Doc arsip; (c) sebelum mengkritik metrik pihak ketiga, coba reproduksi dulu dengan data mereka; kritik hanya bila hasilnya tetap berbeda. Note ditulis sebagai **riset mandiri**: tidak ada bagian "perbandingan dengan Messari/Blockworks"; temuan mereka yang terverifikasi diolah sebagai analisis sendiri dengan sumber disebut.

**4A.6 Porsi fee per aplikasi (L1/L2).** `summary.json → fee_per_aplikasi` memuat porsi fee 30 hari per aplikasi dan kelas halal/nonhalal/tinjau dari `syariah_kategori` + `syariah_override` di config. Semua aplikasi berkelas "tinjau" dengan porsi ≥ 2% wajib diklasifikasi manual (override) sebelum menilai L3/L4. Porsi nonhalal aplikasi menjadi masukan **L4 (penggunaan)** dan, untuk token yang menerima nilai dari aplikasi itu, **L3**. Klasifikasi kategori adalah usulan run; penetapan tetap oleh Komite Syariah.

**4A.7 Pembulatan sebelum label.** Skor fundamental dibulatkan ke 1 desimal **sebelum** menentukan label (6,95–7,04 → 7,0 → Kuat). Sub-skor tetap ditulis 2 desimal di Doc arsip. Skor syariah dibulatkan tanpa desimal sebelum menentukan status.

## 5. Komponen JSON (`rn_build.py`)

Struktur atas: `{"meta": {"title", "header_line"}, "disclaimers": {"A","B","EXEC"}, "pages": [...]}`.
Halaman 1: `{"disclaimer": "EXEC", "exec": {"dateline","name","ticker","logo_file" (atau "logo": data URI / <svg>),"subtitle","chips":[{t,c,dot}],"target":{price,ret,bear,mid,bull},"left":[blok],"right":[blok]}}`.
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
| `thesis` | rows [[label, teks]] | INTI · KENAPA SEKARANG · BISA SALAH BILA |
| `srows` | rows [{tag, title, body, right, tagc, rcolor}] | Pendorong singkat (tag P1–P3) |
| `scen` | label, right, rows [{name,color,prob,target,ret,basis}], note | Ringkasan skenario hal. 1 (nama Optimis/Dasar/Pesimis) |
| `tiles` | items [{label, value, color, sub}] | Ubin angka (prediksi 2030) |
| `tgt` | heads[], rows [{name,color,price,ret,vals[]}] | Target dua lensa |
| `bars` | rows [{label,value,color,display}], max, label_width | Bar pembanding skala linear |
| `split` | segments [{label,value,color,label_color}] (color "dim" = abu) | Bar 100% dua bagian |
| `sankey` | source {label, display}, flows [{label,value,display,color}] | Arus pendapatan |
| `heat` | row_labels, col_labels, values[][], thresholds [bawah, atas], corner, prefix (default "$"), decimals (default 0; pakai 2–3 untuk harga < $10) | Heatmap sensitivitas (merah < bawah ≤ kuning < atas ≤ hijau) |
| `tree` | nodes [{title, sub, color, prob}] | Pohon skenario |
| `timeline` | rows [[tanggal, peristiwa, tag]] | Kalender pendorong |
| `dcard` | tag, title, subtitle, pills [{t,c}], accent, rows [{label, blocks[]}], title_size, mt | Kartu detail pendorong/risiko |
| `stats` | verdict, color, items [{label,value,color,sub}], note | Kotak ringkasan skenario (label default "RINGKASAN SKENARIO") |
| `sharia` | score, verdict, verdict_color, summary, layers [{label,name,icon,icon_color,text,score,pct}], after[], score_label (default "SKOR SYARIAH") | Catatan Syariah (verdict = status v3.1). Cincin skor, bar ambang 40/60/80, dan chip gerbang L1/L3/L4 dibuat otomatis dari `score` tiap lapis (urutan L1–L4) |
| `resources` | items [[nama, domain]], columns | Key resources |
| `spacer` | h | Jarak manual |
| `image` | src (data URI JPEG/PNG, kompres ≤100 KB), alt, caption, plate (`light` = alas putih untuk screenshot grafik), h, mt | Grafik/screenshot sumber primer |
| `donut` | slices [{label, value, color, display, share, bold}], center_top, center_bottom, size, thick | Porsi/komposisi (mis. pangsa jaringan) dengan legenda |
| `steps` | items [{title, text, color}] (3–5 langkah) | Alur proses sederhana (mis. cara kerja tokenisasi) |

### 5.1 Aturan tampilan (selaras dengan situs shariacrypto.id)
- **Warna hanya untuk arti.** Angka biasa ditulis netral (`body`/`white`). Hijau/merah hanya untuk naik/turun dan status, kuning/oranye hanya untuk Bersyarat/Waspada. Jangan mewarnai angka hanya supaya menonjol. Default label kartu, kolom kanan `srows`, keterangan kanan `sub`/`h9`, dan tanggal `timeline` sudah netral.
- **Mono hanya untuk label kecil dan angka.** Nama metrik, isi tabel, dan kalimat memakai font sans. `kv` sudah otomatis: kunci sans, nilai mono.
- **Tanpa emoji.** ✅ ⚠️ ❌ otomatis diganti ikon garis (cek/awas/silang). Emoji lain jangan dipakai.
- **Status pendek jadi pill.** Sel `{"dot": warna, "t": teks}` dengan teks ≤ 22 huruf tampil sebagai pill bertitik ("Positif", "Netral", "Boleh", "Hindari"). Teks yang lebih panjang tetap titik + teks.
- **Angka dan satuan tidak dipisah.** Spasi sebelum juta/miliar/triliun/ribu/jt/rb/th/bln/M/T otomatis jadi spasi tak terputus. Bila `rn_check.js` melaporkan **MELUBER**, lebarkan kolom (`cols`) atau singkat angkanya ($1,44 M); jangan perkecil huruf.
- **Warna note (Rev. 22 Okt 2026).** Kartu `#072E1A` (sedikit lebih gelap dari kartu situs `#0A3D1F`, supaya halaman padat tidak jadi "dinding hijau"), merah teks `#FF8A8A`, biru teks `--info #40C4FF`, sub-judul (2.1, 3.2…) putih lembut. Semua teks di atas kartu ≥ 6,5:1 (WCAG AA). Jangan pakai `darkred`/`--info-solid` untuk teks.
- **Donat.** Teks `center_top` otomatis dikecilkan agar muat di lubang; tetap usahakan ≤ 8 karakter (mis. "1,21 M").

### 5.2 Grafik (v3.2)
- **Jumlah**: 4–8 grafik per note, minimal satu di Bagian 3 (on-chain), satu di Bagian 4 (pendorong/skenario), satu di Bagian 5 (valuasi). Analisis Khusus wajib minimal 1 grafik.
- **Judul = kesimpulan**, bukan nama grafik ("Token yang dilepas turun ±85% mulai Oktober 2026", bukan "Jadwal unlock"). Sub-judul menjelaskan satuan dan cara baca.
- **Sumber + tanggal data** di setiap grafik (kunci `src`). Hitungan sendiri diberi "hitungan Shariacrypto (est.)".
- **Pembuatan**: tulis `data/out/<TICKER>_<tgl>/charts_<TICKER>.json` (format `charts/examples_APT.json`) lalu `python -m charts.render`. Delapan jenis: `line` (indeks vs BTC), `bars` (unlock), `hbars` (fee per aplikasi), `scatter_val` (MC vs pendapatan holder), `fan` (kipas skenario), `projection` (menuju batas suplai), `breakeven` (titik impas deflasi), `supplymap` (peta suplai). Deret dari `scdata` bisa dibaca langsung (`{"csv": ".../series/tvl.csv"}`).
- **Masuk note**: blok `image` dengan `src` data URI (`charts.style.data_uri(path)`), plate `none`. Ukuran tiap PNG ≤ 100 KB (renderer menolak yang lebih besar).
- **Warna = makna** (sama dengan §5.1): hijau = aset yang dibahas/baik/halal · merah = buruk/nonhalal · kuning = ambang, zona, BTC · biru = pembanding netral · oranye = perlu perhatian · abu = konteks/aturan lama. Angka format Indonesia (koma desimal, titik ribuan; "M" = miliar, "jt" = juta, "rb" = ribu).
- Lihat PNG setiap grafik sebelum dimasukkan: tidak ada teks bertumpuk, label tidak terpotong.

## 6. Modul sektor (Metodologi §4)

Tetapkan satu modul sebelum menilai. Modul menentukan metrik pertumbuhan, ukuran nilai ke pemegang, beta asumsi, dan **pembanding wajib (pemimpin kategori)**.

| Modul | Contoh | Metrik utama pertumbuhan | Nilai ke pemegang | Pemimpin kategori |
|---|---|---|---|---|
| Uang / penyimpan nilai | BTC, XMR, ZEC, LTC | Transaksi harian, alamat aktif, nilai transfer | Diganti Kekuatan Moneter (§9.3) | BTC |
| L1 smart contract | ETH, SOL, NEAR, TRX | Fee riil, alamat aktif, TVL | Pembakaran fee dikurangi inflasi staking | ETH |
| DEX | UNI, CRV, AERO, CAKE, RAY | Volume, pendapatan protokol | Distribusi/buyback dikurangi emisi | UNI |
| Perpetual DEX | HYPE | Volume, open interest, pendapatan | Buyback dari pendapatan | HYPE |
| Lending / CDP | AAVE, SKY | Pinjaman beredar, pendapatan bunga bersih | Buyback/distribusi surplus | AAVE |
| Infrastruktur / AI / DePIN | TAO, IO, GEOD | Pendapatan eksternal dari pengguna nyata | Burn/buyback dari pendapatan eksternal | TAO |
| RWA | ONDO, CFG, PRO | Aset tertokenisasi beredar, fee | Bagian fee ke pemegang | ONDO |
| Gaming / NFT | PENGU, NXPC | Pemain aktif, volume NFT, pendapatan game/IP | Bagian pendapatan game/lisensi IP, bila ada | PENGU (sementara) |
| Meme | DOGE, BONK, WIF | Pemegang unik, volume, sebaran pemegang, likuiditas | Umumnya tidak ada | DOGE |
| Token Bursa & CeFi | LEO, OKB, BGB, GT, KCS, WBT, HTX, NEXO (BNB, CRO modul kedua) | Volume bursa, pangsa pasar, aset nasabah (proof of reserves), pengguna aktif | Buyback/burn dari laba bursa atau perusahaan | BNB |
| L2 / Rollup | ARB, MNT, POL, STX, OP | Fee riil, transaksi, TVL, pendapatan sequencer − biaya data ke L1 | Laba sequencer atau buyback ke pemegang; bila tidak ada, tulis terus terang | ARB |
| Jaringan Pembayaran | XRP, XLM | Volume pembayaran lintas negara, stablecoin & aset tertokenisasi di jaringan, alamat aktif | Pembakaran fee dikurangi suplai baru/rilis escrow | XRP |
| Stablecoin & Dolar Sintetis (token protokol) | ENA, WLFI | Suplai stablecoin beredar, pendapatan protokol, sumber imbal hasil cadangan | Fee switch, buyback, distribusi pendapatan | ENA |
| Launchpad | PUMP | Token diluncurkan, volume, pendapatan platform | Buyback dari pendapatan | PUMP |
| Staking Cair (token tata kelola) | LDO, ETHFI, JTO | Aset di-stake lewat protokol, pangsa pasar staking, pendapatan protokol | Buyback/distribusi fee protokol | LDO |

Cek syariah wajib untuk enam modul baru (penetapan tetap oleh Komite Syariah): Token Bursa & CeFi → porsi pendapatan futures, margin, dan produk berbunga masuk L3 · L2 → dinilai seperti L1, status L2 bukan gerbang · Pembayaran → rilis escrow dan pemusatan kepemilikan penerbit · Stablecoin & Dolar Sintetis → sumber imbal hasil (funding rate perpetual, bunga obligasi dalam cadangan) menentukan L3 dan L4 · Launchpad → dominasi perdagangan meme zero-sum dinilai di L4a · Staking Cair → imbalan staking mengikuti posisi staking PoS = bagi hasil. Token tanda terima staking (stETH, weETH, JitoSOL) tetap dikeluarkan (§7.3).

Bila cocok di dua modul, pilih yang pendapatannya terbesar dan sebut modul kedua. Penyesuaian isi Bagian 2:
- **L1 dengan fee & burn:** seperti contoh ETH.
- **Uang/PoW:** 2.3 = pendapatan penambang (subsidi vs fee); 2.4 Sankey biaya keamanan + bar fee vs subsidi + ringkasan Kekuatan Moneter.
- **Protokol dengan pendapatan ke pemegang:** 2.3 per lini produk; Sankey pendapatan → pemegang/treasury/biaya; 2.4 tabel Rantai Nilai ke Pemegang.
- **Tanpa pendapatan on-chain:** tulis terus terang; ganti Sankey dengan bar struktur suplai/emisi.
- Status pemegang (2.1) memakai kategori relevan (bursa, ETF, treasury, tim/VC, unlock, whale, staking).

## 7. Alur kerja run (Senin, Rabu, Jumat)

Kuota: **3 Analisis Perdana per minggu (Senin–Minggu WIB), paling sedikit 2 Jalur Syariah**. Update Kilat tidak dihitung (belum diotomatisasi).

**7.1 Cek kuota.** Dari `RN_Log_Shariacrypto.txt`, hitung baris minggu ini yang memuat "v3.1". Bila sudah 3, hentikan run dan tulis alasannya. Bila sudah ada 1 note Jalur Umum minggu ini, run hari ini **wajib** menghasilkan Jalur Syariah (lihat 7.3 langkah 5).

**7.2 Permintaan pemilik dan klien.** Bila Doc `RN_Permintaan_Shariacrypto` ada, baca barisnya (`YYYY-MM-DD | TICKER | pemilik/klien/anggota | catatan`; baris diawali `#` diabaikan). Urutan prioritas:
1. **pemilik** — permintaan pemilik Shariacrypto. Dikerjakan paling dulu, tanpa batas mingguan selain kuota 3 note per minggu; bila ada beberapa, yang tanggalnya paling lama dulu. Boleh dikerjakan walau minggu itu kuota Jalur Umum sudah terpakai (catat "permintaan pemilik" dan "kuota Jalur Umum terlampaui" di catatan run). Kolom sumber di log: `permintaan pemilik`.
2. **klien** — permintaan klien berbayar. Dikerjakan sesudah permintaan pemilik, **paling banyak satu per minggu** (cek kolom sumber "permintaan klien" di log minggu ini). Permintaan klien berikutnya masuk antrean biasa lewat komponen C.
Permintaan pemilik/klien hanya berlaku untuk ticker yang belum punya note sesudah tanggal permintaan dan tidak punya note < 90 hari; bila punya note < 90 hari, jangan buat Analisis Perdana baru, tulis di pesan akhir bahwa permintaan itu menunggu Update Kilat.

**7.3 Skor prioritas** (bila tidak ada permintaan pemilik atau klien yang didahulukan):
1. Kumpulkan kandidat dari empat daftar:
   - **A. Nilai ke pemegang (40%)**: `defillama.com/holders-revenue`, 25–40 protokol teratas, diurutkan dari MC ÷ holders revenue paling rendah (pakai yang paling konservatif antara TTM dan run-rate 7 hari; cek lonjakan sesaat seperti contoh AERO 5 Okt).
   - **B. Tema aktif (25%)**: RWA dengan pendapatan pemegang, privasi, AI. Ambil aset teratas per tema dari halaman kategori CoinGecko/CMC, urut market cap.
   - **C. Permintaan anggota (20%)**: baris berjenis anggota di `RN_Permintaan_Shariacrypto`, urut tanggal (terlama = peringkat 1).
   - **D. Celah cakupan (15%)**: pakai kolom `Nilai D (0-10)` di Google Sheet `Coverage_Universe_Shariacrypto_v<terbaru>` (folder Drive yang sama; abaikan judul berakhiran `_USANG`). Aset yang sudah terbit note-nya setelah tanggal Sheet (cek log) diberi D = 0. Kolom `Modul sektor` di Sheet menjadi titik awal §6; boleh diganti dengan alasan tertulis di Doc arsip. Aset berstatus `Perlu identifikasi` tidak boleh dipilih sebelum Komite mengisinya. Mulai pembaruan November 2026, universe dan kandidat D mencakup **250 aset market cap terbesar** (keputusan pemilik 20 Okt 2026). Bila Sheet tidak ditemukan, pakai 250 aset market cap terbesar yang belum punya note, urut market cap, dan catat di pesan akhir.
2. Nilai komponen = 10 × (1 − (peringkat − 1) ÷ jumlah kandidat di daftar itu); 0 bila tidak ada di daftar. Skor prioritas = 0,40A + 0,25B + 0,20C + 0,15D.
3. **Keluarkan**: stablecoin, token wrapped/bridged, liquid staking/restaking derivative (dinilai ikut aset induknya); ticker yang sudah punya note **< 90 hari** (cek log lama dan baru); kandidat yang ditolak < 30 hari lalu (baris `# DITOLAK` di log) kecuali datanya berubah material.
4. **Tidak** dikeluarkan karena syariah, volume kecil, atau market cap kecil. Token kecil diberi tier dan penanda risiko (§7.4).
5. Pilih skor tertinggi. Bila 7.1 mewajibkan Jalur Syariah: cek cepat gerbang L1 dan L3 (§9.4) kandidat teratas; bila jelas gagal, turun ke kandidat berikutnya. Bila setelah penilaian penuh ternyata tetap Jalur Umum, note tetap terbit dan catat "kuota Jalur Umum terlampaui" di catatan run.
6. Tulis tabel skrining (kandidat, A/B/C/D, skor, keputusan/alasan) di Doc arsip; tambahkan baris `# DITOLAK YYYY-MM-DD | TICKER | alasan` ke log untuk kandidat yang ditolak karena alasan selain skor.
7. Run **tidak boleh** menafsirkan ulang aturan ini. Kasus yang tidak tercakup dicatat sebagai pertanyaan untuk Komite di pesan akhir.

**7.4 Tier ukuran** (market cap): Aset Besar > $5 miliar · Aset Menengah $500 juta–$5 miliar · Aset Kecil $50–500 juta · Aset Mikro < $50 juta. Aset Kecil wajib menampilkan volume harian, FDV/MC, unlock 12 bln di Metrik utama. Aset Mikro menambah perkiraan slippage transaksi $10.000, konsentrasi 10 pemegang terbesar, dan peringatan "risiko likuiditas tinggi" di hal. 1.

**7.5 Langkah membangun**
1. `scdata.fetch` → baca `checks.md`, rekonsiliasi (§4A) → snapshot data (§8) → modul sektor (§6) → syariah & jalur (§9.4) → skor fundamental (§9.3) → Rantai Nilai → skenario (§4) → P/R & dasbor → label dari matriks.
2. Grafik (§5.2) → tulis `content_<TICKER>.json` (salinan struktur `contoh_ETH.json` + halaman on-chain dari `contoh_onchain_BTC.json`), bangun, jalankan `rn_check.js` sampai semua halaman OK dan tidak ada baris MELUBER (aturan tampilan §5.1). Lihat PNG minimal hal. 1, halaman Sankey/Rantai Nilai, valuasi, dan risiko.
3. Jalankan daftar periksa §8.4.
4. Terbitkan note sebagai artifact baru (capabilities `{"artifact": {}, "downloads": true}`), judul `Shariacrypto Research Note — <Nama> (<TICKER>) — <tgl>`.
5. Arsip dan log (§8).

## 8. Arsip, log, snapshot, pengungkapan

**8.1 Snapshot data** — `scdata.fetch` membuat `snapshot_<TICKER>_<tgl>.csv` otomatis dari API. Angka manual (hasil riset primer, komponen suplai) ditambahkan ke file yang sama sebelum diunggah. Sebelum menulis, simpan semua angka yang dipakai ke `snapshot_<TICKER>_<YYYY-MM-DD>.csv` di folder Drive (text/csv, tanpa konversi), kolom `metrik,nilai,satuan,sumber,waktu_data`. Angka di note harus cocok dengan snapshot. Angka manual (dibaca dari grafik/berita) diberi sumber `manual: <sumber>`.

**8.2 Doc arsip = lampiran metodologi** — Google Doc `RN_<TICKER>_<YYYY-MM-DD> — Shariacrypto Research Note <Nama>` (tulis mata uang sebagai "USD", bukan tanda $: konversi Markdown ke Google Doc menghapus teks di antara dua tanda $): link artifact; versi metodologi; jalur & tier & modul; empat label + sikap; skenario (peluang, target, beta, alfa per skenario dengan tautan P/R, sumber Pandangan Pasar); cek kelipatan; P1–P3 & R1–R3; Rantai Nilai lengkap; **sub-skor fundamental per rubrik dengan angka & sumber**; tanda bahaya; skor syariah per lapis + alasan; status 6 aktivitas; pembanding syariah; tabel skrining; nama file snapshot; data N/A dan sumber yang gagal; **riwayat revisi**.

**8.3 Log**
- `RN_Log_Shariacrypto.txt` — baris baru: `YYYY-MM-DD | TICKER | Nama | Jalur | Tier | Fundamental skor·label | Harga rasio·label | Syariah status·skor | Sikap | sumber pemilihan | v3.1 | link artifact | link Doc`. Baris lama tidak diubah.
- `RN_Peluang_Shariacrypto.txt` — satu baris per P dan R: `tgl terbit | TICKER | kode | peluang | tenggat | indikator → sasaran | hasil` (kolom hasil dikosongkan; diisi saat jatuh tempo untuk Brier score).
- Coverage Universe tidak diubah oleh run. Sheet diperbarui bulanan (bersamaan dengan Pandangan Pasar) oleh Komite atau run terpisah: versi baru dibuat, versi lama diberi akhiran `_USANG_sebelum_<YYYY-MM-DD>`.
- Konektor Drive tidak bisa mengedit file: buat ulang file berisi isi lama + baris baru, lalu ganti judul file lama menjadi `<nama>_USANG_sebelum_<YYYY-MM-DD>.txt`. File yang belum ada dibuat dengan baris header diawali `#`.

**8.4 Daftar periksa sebelum terbit**
- Semua angka cocok dengan snapshot; peluang skenario berjumlah 100% dan kelipatan 5%.
- Label dan sikap sesuai tabel §4 dan matriks; tidak ada kata terlarang (§4 Label).
- Tidak ada karakter escape, tanda baca rusak, atau angka tanpa satuan; angka besar memakai juta/miliar/triliun.
- Pengungkapan kepemilikan terisi di disclaimer EXEC; "Metodologi v3.1" ada di dateline.
- Glosarium memuat semua istilah teknis; selisih > 20 poin dengan pembanding syariah sudah dijelaskan; Harga Perkiraan > +30% sudah disertai paragraf "Mengapa pasar keliru menilai".

**8.5 Pengungkapan kepemilikan** — pakai Doc `Pengungkapan_Kepemilikan_Shariacrypto` bila ada. Bila tidak ada, pakai daftar baku Investment Tiers Grup Eksklusif: **BTC, XMR, TAO, ETH, SOL, HYPE, TON, LTC, NEAR, SPX, ONDO**. Aset dalam daftar: "Pengungkapan: Grup Eksklusif Shariacrypto memegang aset ini sebagai investasi jangka panjang." Aset di luar daftar: "Pengungkapan: per tanggal data, aset ini tidak termasuk daftar kepemilikan Grup Eksklusif Shariacrypto."

## 9. Penilaian (Metodologi v3.1)

Semua skor dihitung di dalam run, dengan atau tanpa laporan FA. Laporan FA hanya bahan; skornya tidak disalin. Semua skor diberi "(est.)" di hal. 1 dan Doc arsip.

### 9.1 Pemilihan aset — lihat §7.3.

### 9.2 Data dasar & sumber
- Harga/MC/suplai: CoinGecko **dan** CoinMarketCap; selisih suplai > 3% → pakai yang cocok dengan explorer, catat selisihnya.
- Sumber per kebutuhan (Metodologi §5.1): fee & pendapatan → Token Terminal, Artemis, pembanding DefiLlama · earnings setelah insentif → Token Terminal, atau hitung emisi × harga · Nilai Diterima Pemegang → Dune, explorer, dashboard/laporan resmi protokol · emisi & unlock → Tokenomist, dokumentasi resmi, kontrak vesting · metrik modul Uang → Glassnode, CryptoQuant (bagian gratis), explorer, mempool.space · riset pembanding → Messari, Blockworks Research.
- Halaman yang butuh login/berbayar dicatat sebagai "tidak bisa diakses" di catatan run; jangan dicoba berulang.
- Aktivitas pengembang: **GitHub langsung** (kontributor aktif dan commit 12 bulan di repo inti). Median kategori dihitung dengan cara yang sama dari pemimpin kategori + minimal 4 proyek teratas modul. Sampai sheet referensi median tersedia, hitung di run; bila tidak sempat, sub-skor N/A.

### 9.3 Skor fundamental 4 dimensi

`Skor = 0,30 T + 0,30 J + 0,25 N + 0,15 R`. Sub-skor 1–10 memakai titik acuan 2/5/8/10 (interpolasi di antaranya); skor dimensi = rata-rata sub-skor yang tersedia. Sub-skor tanpa data = N/A (bobot dinormalkan); bila > 1/3 sub-skor satu dimensi N/A, keyakinan paling tinggi Sedang. Penyimpangan dari rubrik maks. 1 poin dengan alasan satu kalimat di Doc arsip.

**T — Tokenomics (30%)**

| Sub-skor | Ukuran | 2 | 5 | 8 | 10 |
|---|---|---|---|---|---|
| Laju penambahan suplai | Inflasi bersih 12 bln setelah pembakaran | > 15% | 5–10% | 1–3% | ≤ 0,5% / deflasi |
| Tekanan pelepasan token | Unlock 12 bln ke depan, % suplai beredar | > 30% | 10–20% | ≤ 5% | 0% |
| Rasio FDV/MC | FDV ÷ MC | > 5× | 2–3× | ≤ 1,3× | 1,0× |
| Sebaran kepemilikan | 10 pemegang terbesar di luar bursa & kontrak, % beredar | > 70% | 40–55% | 20–30% | < 15% |
| Alokasi orang dalam | Tim + investor, % suplai awal | > 50% | 30–40% | ≤ 20% | 0% |
| Kegunaan token | Peran token | Tanpa fungsi / tata kelola saja | Tata kelola + bagi hasil | Fungsi inti, bisa diganti | Fungsi inti, tak tergantikan |

**J — Jaringan & Bisnis (30%)**

| Sub-skor | Ukuran | 2 | 5 | 8 | 10 |
|---|---|---|---|---|---|
| Pertumbuhan penggunaan | Perubahan 12 bln metrik utama modul | < −40% | −10% s.d. +10% | +25% s.d. +50% | > +100% |
| Tren pendapatan | Kuartal terakhir ×4 vs 12 bln sebelumnya | < −40% | −10% s.d. +10% | +25% s.d. +50% | > +100% |
| Kualitas aktivitas | Porsi aktivitas organik (bukan insentif/subsidi) | < 25% | 40–60% | 70–90% | ≥ 90% |
| Aktivitas pengembang | Kontributor aktif 12 bln ÷ median kategori | < 0,3× | ≈ 1× | 1–2× | ≥ 2× |
| Posisi kompetitif | Pangsa pasar di kategori | < 2% | Peringkat 4–10 / 5–15% | Peringkat 2–3 / 15–40% | Peringkat 1 & ≥ 40% |
| Tingkat desentralisasi | Porsi 3 entitas terbesar di konsensus/tata kelola | > 85% | 50–70% | 33–50% | < 33% |

**N — Nilai ke Pemegang (25%)** (modul Uang: diganti Kekuatan Moneter)

| Sub-skor | Ukuran | 2 | 5 | 8 | 10 |
|---|---|---|---|---|---|
| Mekanisme nilai | Jalur nilai ke pemegang | Tidak ada | Fee belum disalurkan / fee switch belum aktif | Buyback diskresioner | Distribusi tunai / buyback-burn terprogram |
| Hasil bersih pemegang | Hasil Bersih Pemegang ÷ MC | Negatif | 0–1% | 3–5% | ≥ 8% |
| Rasio realisasi | Nilai Diterima ÷ holders revenue DefiLlama | < 15% | 30–50% | 60–90% | ≥ 90% |
| Stabilitas pendapatan | Koefisien variasi pendapatan bulanan 12 bln | > 1,2 | 0,6–0,8 | 0,2–0,4 | < 0,2 |

**Kekuatan Moneter (pengganti N untuk modul Uang, 25%)** — ambang absolut, bukan relatif terhadap BTC.

| Sub-skor | Ukuran | 2 | 5 | 8 | 10 |
|---|---|---|---|---|---|
| Kepemilikan jangka panjang | Suplai tak berpindah ≥ 1 thn | < 20% | 35–50% | 55–65% | ≥ 70% |
| Akses pasar | Bursa utama + volume ÷ MC | Hampir tanpa akses fiat | Beberapa bursa, terbatas | Bursa besar di banyak yurisdiksi | Tersedia luas + produk teregulasi |
| Adopsi alat bayar | Nilai transfer, pedagang | Hampir tidak dipakai | Ceruk tertentu | Luas di ceruknya | Lintas negara & ceruk |
| Ketahanan sejarah | Umur & pemulihan krisis | < 3 thn | 3–6 thn, pulih sekali | 7–10 thn, pulih beberapa kali | > 10 thn, banyak siklus |

- Data tak tersedia (mis. suplai tak berpindah untuk XMR karena privasi) → N/A, bobot dinormalkan.
- **Delisting bursa besar untuk aset modul Uang (kasus utama XMR) hanya dinilai di Akses pasar**, tidak di Risiko Regulasi.

**R — Risiko (15%)** — `R = 10 − rata-rata(keparahan × peluang ÷ 10)` untuk 8 kategori: kontrak pintar/protokol · regulasi · likuiditas · tim/tokoh kunci · konsentrasi · kompetisi · jembatan/kustodi · tata kelola. Makro **tidak** dinilai di sini. Acuan keparahan: 2 gangguan kecil · 5 harga turun 30–50% · 8 kehilangan sebagian besar nilai · 10 protokol berhenti. Acuan peluang (12 bln): 2 < 10% · 5 ±30% · 8 > 60%. Likuiditas: volume ÷ MC ≥ 5% → peluang 2; 1–2% → 5; < 0,3% → 8.

**Tanda bahaya** (Ya/Tidak): tim anonim · tanpa audit · tim/VC > 30% · FDV/MC > 5× · umur < 6 bulan · tiruan · tanpa kegunaan · janji imbal hasil · pendiri menjual besar-besaran. **≥ 3 aktif → skor dibatasi maks. 5,49 (Lemah).**

Dari laporan FA lama: jangan memakai rumus konversi composite lama; nilai ulang sub-skor dengan rubrik ini.

### 9.4 Syariah 4 lapis

**Posisi ijtihad yang dikunci:** spekulasi & volatilitas bukan kriteria maysir · staking PoS = bagi hasil, bukan riba · Value-Source Test = uji utama token tata kelola/utilitas · L2 bukan gerbang · memegang USDT/USDC dinilai dengan i'anah 'ala al-itsm dan sadd al-dzari'ah (posisi wara' minoritas).

| Lapis | Bobot | Gerbang | Titik acuan |
|---|---|---|---|
| L1 Infrastruktur | 30 | ≥ 12 | 30 protokol inti tanpa riba/maysir · 20 komponen berbunga di luar fungsi inti · 12 komponen berbunga signifikan, bukan inti · < 12 fungsi inti berbunga/judi |
| L2 Utilitas token | 30 | — | 30 alat tukar, gas, ujrah/ju'alah jelas · 20 tata kelola + bagi hasil tercampur · 10 hak atas pendapatan yang sebagian besar berbunga · 0 utilitas inti tidak halal |
| L3 Sumber nilai | 10 | ≥ 4 | 10 = 0% non-halal · 8 = < 5% (cukup tathir) · 6 = 5–15% · 4 = 15–30% · < 4 = > 30% |
| L4 Penggunaan | 30 | ≥ 12 | 30 penggunaan riil halal dominan · 20 riil ada, spekulasi/subsidi besar · 12 halal & non-halal berimbang · < 12 dominan non-halal (judi, leverage) |

- Pengurangan L4 karena pemakaian ilegal sebagian pengguna diukur dari **porsi aktivitas aset itu sendiri**, bukan porsi pasar gelap yang menerimanya: < 5% → −0–2 · 5–20% → −3–6 · > 20% → −7–12. Porsi tidak diketahui → pakai pengurangan terakhir yang ditetapkan Komite Syariah untuk aset itu (lihat note terakhir/Doc arsip); bila belum pernah, −0 dan tulis "perlu penetapan Komite Syariah".
- **Status**: lolos semua gerbang & total ≥ 80 → Sesuai Syariah · 60–79 → Halal Bersyarat · 40–59 → Banyak Catatan · < 40 atau gagal gerbang mana pun → Tidak Sesuai Syariah. Dua status pertama = **Jalur Syariah**; dua terakhir = **Jalur Umum**.
- **Keyakinan syariah**: Tinggi (sumber pendapatan terverifikasi dari data protokol) · Sedang (sebagian perkiraan) · Rendah (porsi non-halal perkiraan kasar).
- **Status 6 aktivitas** (Boleh / Bersyarat + syarat / Hindari): beli & simpan · staking · penyedia likuiditas · pinjam-meminjam · perpetual/leverage · ETF/produk turunan.
- **Tathir**: atas hasil yang diterima (bagi hasil, imbalan staking, bagian fee) sebesar porsi non-halal L3. Untuk protokol dengan **buyback**: tathir per tahun = nilai kepemilikan × (buyback 12 bln ÷ MC) × porsi non-halal, dibayar tahunan. Porsi non-halal diambil dari sumber dana buyback bila protokol memisahkannya; bila tidak, dari L3. Tulis contoh per $1.000 kepemilikan di Catatan Syariah.
- **Pembanding**: HalalScreener, Sharlife, Islamic Finance Guru, Practical Islamic Finance, CryptoUmmah (tulis N/A bila tidak ada) dengan tanggal. Status berbeda dari pembanding utama atau selisih > 20 poin → paragraf penjelasan sumber perbedaan.
- Selalu "bukan fatwa".

## 10. Pelajaran teknis dari run sebelumnya
- (v3.2) Di Claude Code dengan jaringan Custom, endpoint API **bisa** dipakai lewat `scdata`; catatan "API diblokir" di bawah hanya berlaku untuk lingkungan Cowork lama.
- (v3.2) CoinGecko "1y" di ringkasan halaman pernah salah (+74% padahal −76,9%): pakai `summary.json → beta.return_asset_pct` yang dihitung dari deret harga.
- WebFetch ke halaman situs DefiLlama/CoinGecko/CMC berhasil; endpoint API (`api.coingecko.com`, `api.llama.fi`, `api.blockchair.com`) diblokir — jangan buang token mencobanya.
- Ringkasan WebFetch bisa salah label (mis. "1 thn +61,8%" padahal −63,7%): cek silang angka penting dengan sumber kedua.
- Heatmap harga < $10: isi `"decimals": 3` di blok `heat`.
- Sankey dengan aliran < 1% tidak terlihat dan labelnya bertumpuk: keluarkan dari Sankey, sebutkan di note.
- Klaim di media sosial (mis. "whale beli X") tanpa dompet/sumber yang bisa dicek tidak dipakai sebagai data.
- Logo koin: hanya `raw.githubusercontent.com` yang terbukti bisa diunduh dari lingkungan run (CoinGecko, cryptologos, Wikimedia, jsDelivr diblokir); karena itu `rn_logo.py` memakai repo GitHub terbuka.
- Alamat situs di footer note adalah **shariacrypto.id** (diatur di `rn_build.py`); jangan menulis domain lain di isi note.

## 11. Penyesuaian, veto, dan revisi (Research Independence Policy)

- Komite Rating dan Komite Syariah masing-masing beranggotakan dua orang; bila keduanya tidak sepakat, pemilik memutuskan. Run otomatis berperan sebagai penulis.
- Run menghitung **hasil rubrik** dengan jujur: sub-skor, peluang, dan alfa diisi dari data dan rubrik. Penyesuaian di luar rubrik bukan tugas run.
- Setelah note terbit, penilaian boleh diubah lewat tiga jalur: **Tinjauan** (pemilik/komite mengirim catatan; penulis menanggapi tertulis dalam 2 hari kerja), **Penyesuaian kualitatif** komite (skor fundamental ±1,0; peluang tiap skenario ±10 poin; skor syariah ±10; alasan 1–3 kalimat), dan **Veto** pemilik (final, alasan satu kalimat). Data baru atau koreksi hitungan cukup lewat Update Kilat.
- Bila run diminta menerapkan tinjauan, penyesuaian, atau veto (prompt atau Doc instruksi dari pemilik), run menerapkannya, mencatat **hasil rubrik semula** dan penilaian akhir di riwayat revisi Doc arsip, tanpa menampilkannya di note untuk customer. Versi lama diberi akhiran "USANG".
- **Catatan Pandangan Berbeda** bersifat sukarela: kartu (`card`, label "CATATAN PANDANGAN BERBEDA") di akhir Bagian 6 atau cukup di Doc arsip.
- Yang tetap tidak boleh: menghapus hasil rubrik semula dari Doc arsip, menerbitkan note tanpa pengungkapan kepemilikan, dan menjanjikan hasil penilaian kepada klien atau proyek.
- Perubahan bobot, rubrik, ambang, atau label hanya lewat versi metodologi baru; PANDUAN diperbarui pada hari yang sama.

## 12. Yang belum diotomatisasi (jangan dikerjakan run ini)

Update Kilat, Update Kuartalan, Rapor Kinerja Riset, dan Pandangan Pasar Bulanan disusun terpisah. Run ini hanya menghasilkan Analisis Perdana, tetapi wajib mengisi `RN_Peluang_Shariacrypto.txt` dan Dasbor Pantauan agar tahap-tahap itu bisa berjalan.
