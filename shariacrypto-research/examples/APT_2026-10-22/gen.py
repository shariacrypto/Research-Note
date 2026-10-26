# -*- coding: utf-8 -*-
import json
W = lambda t: f'<strong style="color: var(--white);">{t}</strong>'
logo_note = 'Logo: Trust Wallet Assets'

def T(t, c='white', s=None):
    d = {"t": t, "c": c}
    if s: d["s"] = s
    return d
def N(n, c='body', b=False, s=None):
    d = {"n": n, "c": c}
    if b: d["b"] = True
    if s: d["s"] = s
    return d
def D(dot, t): return {"dot": dot, "t": t}


import base64 as _b64
def IMG(p): return "data:image/png;base64," + _b64.b64encode(open(p,'rb').read()).decode()

pages = []

# ---------------- HAL 1 ----------------
pages.append({"disclaimer": "EXEC", "exec": {
  "dateline": "Data 21–22 Okt 2026 · harga ±08.30 WIB 22 Okt · <span style=\"color: var(--gold-500);\">Metodologi v3.1</span>",
  "name": "Aptos",
  "ticker": "APT",
  "logo_file": "logo_APT.txt",
  "subtitle": "APT · Aset Menengah · Jalur Syariah · L1 smart contract · #91",
  "chips": [
    {"t": "Fundamental: Kuat · 7,0", "c": "green", "dot": True},
    {"t": "Harga: Murah · rasio 3,1×", "c": "green", "dot": True},
    {"t": "Syariah: Halal Bersyarat · 74", "c": "warning"},
    {"t": "Beli Bertahap · keyakinan rendah", "c": "green"}
  ],
  "target": {"price": "$1,095", "ret": "+33,1% dari $0,822", "bear": "Pesimis $0,445", "mid": "Perkiraan $1,019", "bull": "Optimis $1,531", "label": "TARGET 12 BULAN · SKENARIO DASAR"},
  "left": [
    {"type": "h9", "num": "1.1", "title": "TESIS INVESTASI"},
    {"type": "thesis", "rows": [
      ["INTI", "APT adalah token gas dan staking jaringan Aptos. Sejak Maret 2026 suplai dibatasi 2,1 miliar, imbalan staking dipotong jadi 2,6%, dan seluruh fee dibakar. Tetapi yang dibakar baru ±174 ribu APT sebulan, sedangkan staking mencetak ±1,5 juta."],
      ["KENAPA SEKARANG", "Jatah tim dan investor habis terbuka 12 Okt 2026. Unlock setahun ke depan tinggal ±21 juta APT, dari ±135 juta tahun ini. Harga sudah −77% setahun dan −96% dari puncak."],
      ["BISA SALAH BILA", "Decibel, sumber 98% transaksi, kehilangan volume, atau ekosistem terus mengecil (TVL DeFi $43 juta). Deflasi butuh pembakaran ±10 kali lipat dari sekarang."]
    ]},
    {"type": "h9", "num": "1.2", "title": "PENDORONG SINGKAT", "mt": 10},
    {"type": "srows", "rows": [
      {"tag": "P1", "title": "Unlock tim &amp; investor selesai", "body": "suplai beredar ≤915 juta APT pada 22 Okt 2027.", "right": "Peluang 70%<br>Okt 2027"},
      {"tag": "P2", "title": "Pembakaran fee naik tiga kali", "body": "dibakar per 30 hari naik dari ±174 ribu ke ≥500 ribu APT.", "right": "Peluang 25%<br>Sep 2027"},
      {"tag": "P3", "title": "Stablecoin kembali tumbuh", "body": "stablecoin di Aptos naik dari $949 juta ke ≥$1,5 miliar.", "right": "Peluang 35%<br>Jun 2027"}
    ]},
    {"type": "h9", "num": "1.3", "title": "RINGKASAN SKENARIO", "mt": 10},
    {"type": "scen", "label": "HARGA MURAH · RASIO ±3,1×", "right": "Harga Perkiraan $1,019 (+24,0%)", "rows": [
      {"name": "Optimis", "color": "green", "prob": "20%", "target": "$1,531", "ret": "+86,2%", "basis": "BTC +57,7% × 1,32 + alfa 10 (P2)"},
      {"name": "Dasar", "color": "info", "prob": "55%", "target": "$1,095", "ret": "+33,1%", "basis": "BTC +21,3% × 1,32 + alfa 5 (P1)"},
      {"name": "Pesimis", "color": "red", "prob": "25%", "target": "$0,445", "ret": "−45,9%", "basis": "BTC −27,2% × 1,32 − alfa 10 (R1)"}
    ], "note": "Peluang dari Pandangan Pasar Oktober 2026; target = harga akhir 12 bulan. Rasio = potensi naik $0,291 ÷ potensi turun $0,094."},
    {"type": "h9", "num": "1.4", "title": "GAMBARAN HARGA APT 2030", "mt": 10, "right": "bukan target 12 bulan"},
    {"type": "tiles", "items": [
      {"label": "KONSERVATIF · 0,10%", "value": "±$0,70"},
      {"label": "MODERAT · 0,15%", "value": "±$1,57"},
      {"label": "OPTIMIS · 0,25%", "value": "±$3,91"}
    ]},
    {"type": "note", "html": "Nilai pasar L1 2030 ($0,8/1,2/1,8 triliun) × porsi Aptos ÷ ±1,15 miliar APT (est.)."}
  ],
  "right": [
    {"type": "h9", "title": "METRIK UTAMA", "mb": 2},
    {"type": "kv", "rows": [
      ["Harga", "$0,822"],
      ["Market cap", "$726,5 juta"],
      ["Dari puncak $19,90", "−95,9%", "red"],
      ["Return 52 minggu", "−76,9% (BTC −27,5%)", "red"],
      ["Volume 24 jam", "$75,2 juta (10,3% MC)"],
      ["FDV ÷ MC", "1,37× (2,38× ke batas)"],
      ["Unlock 12 bln ke depan", "±21 juta (2,4%)"],
      ["APT baru dari staking", "±1,5 juta/bln"],
      ["APT dibakar", "±174 ribu/bln"],
      ["Suplai bersih", "+1,3%/th (est.)"],
      ["Fee jaringan 30 hari", "$141,4 ribu"],
      ["Lama balik modal", "±420–840 th (est.)"],
      ["Beta terhadap BTC", "1,32"],
      ["Batas suplai", "2,1 miliar (terisi 58%)"],
      ["Fundamental", "7,0 · Kuat", "green"]
    ]},
    {"type": "h9", "title": "TARGET 12 BULAN · DUA CARA HITUNG", "mb": 6, "mt": 12},
    {"type": "tgt", "heads": ["MC TERSIRAT", "BALIK MODAL", "PELUANG"], "rows": [
      {"name": "OPTIMIS", "color": "green", "price": "$1,531", "ret": "+86,2%", "vals": ["$1,44 M", "±834 th", "20%"]},
      {"name": "DASAR", "color": "info", "price": "$1,095", "ret": "+33,1%", "vals": ["$1,03 M", "±597 th", "55%"]},
      {"name": "PESIMIS", "color": "red", "price": "$0,445", "ret": "−45,9%", "vals": ["$417 juta", "±243 th", "25%"]}
    ]},
    {"type": "note", "html": "M = miliar. MC tersirat = target × ±938 juta APT beredar (Okt 2027, est.). Balik modal = MC ÷ fee yang dibakar per tahun ($1,72 juta, laju 30 hari)."},
    {"type": "h9", "title": "DERIVATIF TERBARU · 21 OKT", "mb": 2, "mt": 12},
    {"type": "kv", "rows": [
      ["Harga 24 jam", "+9,7%", "green"],
      ["Open interest Binance", "$21,2 juta (−12,4%)"],
      ["Funding 8 jam", "0,01% (netral)"]
    ]},
  ]
}})

# ---------------- HAL 2: Business highlight holder ----------------
pages.append({"label": "Business highlight - holder", "subtitle": "Business highlight: holder &amp; institusi", "blocks": [
  {"type": "bigsec", "num": "2", "title": "Business Highlight", "mt": 20},
  {"type": "text", "html": "Siapa yang memegang APT, bagaimana kepemilikannya berubah, dan dari mana jaringan Aptos mendapat uang.", "muted": True, "mb": 4},
  {"type": "sub", "num": "2.1", "title": "SIAPA HOLDER APT &amp; PERUBAHANNYA"},
  {"type": "table", "cols": "128px 92px minmax(0px,1fr) minmax(0px,1fr) 150px", "header": ["KATEGORI", "KINI", "SEBELUMNYA", "PERUBAHAN", "STATUS"], "rows": [
    [T("Suplai total"), N("1,21 miliar", s="22 Okt"), N("±1,196 miliar", s="Feb 2026"), N("+±14 juta", s="dari staking"), D("gold", "Naik ±1,3% per tahun")],
    [T("Suplai beredar"), N("883,3 juta", s="73% total"), N("871,0 juta", s="30 Sep"), N("+12,3 juta", s="3 minggu"), D("gold", "Termasuk unlock 12 Okt")],
    [T("Di-stake"), N("±763 juta", s="±63% total"), N("N/A", "muted"), N("N/A", "muted"), D("green", "Imbalan kini 2,6%/th")],
    [T("Dikunci permanen yayasan"), N("210 juta", s="17,4% total"), N("0", "muted", s="sebelum Feb 2026"), N("+210 juta", "green"), D("green", "Tidak akan dijual")],
    [T("Belum terbuka", s="termasuk 210 juta dikunci"), N("±326,7 juta", s="27% total"), N("331,7 juta", s="30 Sep"), N("±−1,75 juta/bln", s="Messari"), D("gold", "Sisa ±117–125 juta s.d. 2032")],
    [T("Jatah tim + investor awal"), N("324,8 juta", s="32,5% suplai awal"), N("±6,77 juta/bln", "muted", s="terbuka s.d. Sep"), N("100% terbuka", "green"), D("green", "Jadwal selesai 12 Okt 2026")],
    [T("Dibakar (kumulatif)"), N("±2,0 juta", s="0,17% total"), N("±1,8 juta", s="14 Sep"), N("+±0,2 juta", s="5 minggu"), D("gold", "Masih kecil")],
    [T("Bursa (cadangan)"), N("N/A", "muted"), N("N/A", "muted"), N("N/A", "muted"), D("muted", "Tidak ada data publik")]
  ], "hl": [5]},
  {"type": "text", "html": "Sumber: CoinGecko/CoinMarketCap (22 Okt), dasbor suplai Aptos (21 Okt), Everstake (30 Sep), Crypto Briefing (14 Sep). Angka di-stake dan yang belum terbuka bisa tumpang tindih karena token yang masih terkunci juga bisa di-stake.", "size": 9, "muted": True, "mt": 6},
  {"type": "card", "label": "RINGKASAN", "blocks": [
    {"type": "text", "html": f"Mulai Oktober 2026, {W('tim dan investor awal tidak lagi punya token terkunci')}. Dari ±326,7 juta APT yang belum terbuka, 210 juta dikunci permanen di staking; hanya ±117–125 juta yang masih dilepas sampai 2032, sekitar ±1,75 juta per bulan (Messari). Jadi suplai yang benar-benar bisa dijual makin kecil, tetapi yayasan tetap menjadi holder paling dominan."}
  ], "mt": 8},
  {"type": "sub", "num": "2.2", "title": "DUKUNGAN INSTITUSI", "mt": 16},
  {"type": "table", "cols": "128px 88px minmax(0px,1fr)", "header": ["PIHAK", "PERAN", "CATATAN"], "rows": [
    [T("Aptos Foundation"), "Yayasan", "Mengunci 210 juta APT permanen; bersama Aptos Labs menyiapkan dana &gt;$50 juta untuk produk, riset, dan mitra trading/AI"],
    [T("Bitwise"), "Manajer aset", "Mengajukan S-1 untuk ETF spot APT di AS (Mar 2025). Status persetujuan per Okt 2026: N/A, belum ada keputusan yang bisa kami verifikasi"],
    [T("BlackRock · Franklin Templeton · Ondo"), "Penerbit RWA", "Dana BUIDL, FOBXX, dan USDY sudah ada di Aptos. Nilai RWA aktif di Aptos $761,3 juta (DefiLlama, 21 Okt)"],
    [T("Securitize"), "Tokenisasi", "Aplikasi dengan fee 30 hari terbesar di Aptos ($623 ribu)"],
    [T("Yellow Card · Bitso · coins.ph"), "Pembayaran", "Menghubungkan pengguna di Afrika, Amerika Latin, dan Asia Tenggara ke stablecoin di Aptos"],
    [T("Decibel"), "Bursa perpetual", "Diinkubasi Aptos Labs; aktif sejak Feb 2026; volume ±$53,6 juta per hari"]
  ]},
  {"type": "card", "label": "CATATAN", "blocks": [
    {"type": "text", "html": "Dukungan institusi Aptos lebih banyak berupa produk yang “tinggal” di jaringannya (dana tokenisasi, stablecoin), bukan pembeli APT. Belum ada ETF APT atau perusahaan publik yang menimbun APT dalam jumlah yang dilaporkan."}
  ], "mt": 8}
]})

# ---------------- HAL 3: revenue & rantai nilai ----------------
pages.append({"label": "Business highlight - revenue", "subtitle": "Business highlight: pendapatan &amp; rantai nilai", "blocks": [
  {"type": "sub", "num": "2.3", "title": "DARI MANA APTOS MENDAPAT UANG", "mt": 14, "right": "DefiLlama · dasbor Aptos · 21 Okt 2026"},
  {"type": "text", "html": "Aptos menjual ruang blok. Setiap transaksi membayar gas dengan APT, dan sejak Maret 2026 seluruhnya dibakar. Validator dibayar dengan APT baru dari staking.", "mb": 8},
  {"type": "table", "cols": "140px 110px 120px minmax(0px,1fr)", "header": ["ALIRAN", "NILAI", "MENGALIR KE", "PENGGERAK UTAMA"], "rows": [
    [T("Gas fee jaringan", s="dibakar 100%"), N("$141,4 ribu", "white", True, "30 hari · $1,72 juta/th"), "Semua holder, lewat pembakaran", "Jumlah transaksi (9,7–14,35 juta/hari) × fee rata-rata ±$0,0005"],
    [T("APT baru dari staking", s="biaya keamanan"), N("±1,5 juta APT/bln", s="±$14,8 juta/th"), "Staker &amp; validator", "Imbalan 2,6% per tahun atas APT yang di-stake"],
    [T("Fee aplikasi"), N("±$1,16 juta", "body", s="30 hari (est.)"), "Aplikasi (Securitize, Decibel, Echelon, DEX)", "Tokenisasi, perpetual, pinjaman, pertukaran"],
    [T("Total yang dibayar pengguna"), N("±$1,30 juta", "white", True, "30 hari"), "", "Jaringan hanya menerima ±11%"]
  ], "hl": [3]},
  {"type": "grid", "items": [
    {"type": "card", "label": "SIAPA MENIKMATI BIAYA DARI PENGGUNA", "blocks": [
      {"type": "split", "segments": [{"label": "Aplikasi ±$1,16 juta", "value": 89, "color": "dim"}, {"label": "Dibakar $141 ribu", "value": 11, "color": "green", "label_color": "green"}]},
      {"type": "text", "html": "Dari ±$1,30 juta fee 30 hari, hanya ±11% yang sampai ke holder APT lewat pembakaran.", "mt": 5}
    ]},
    {"type": "card", "label": "PERKEMBANGAN TERBARU", "blocks": [
      {"type": "ul", "items": [
        f"{W('Maret 2026:')} gas naik 10×, imbalan staking 5,19% → 2,6%, batas suplai 2,1 miliar (Proposal #183–#185).",
        f"{W('30 hari terakhir:')} dibakar 174.210 APT; burn menutup ±11% APT baru (sebelum Maret ±0,2%).",
        f"{W('20 Okt:')} mempool terenkripsi aktif di mainnet."
      ]}
    ]}
  ]},
  {"type": "sub", "num": "2.4", "title": "RANTAI NILAI KE HOLDER (12 BULAN)", "mt": 10},
  {"type": "grid", "mt": 0, "cols": "minmax(0px,1.2fr) minmax(0px,1fr)", "items": [
    {"type": "card", "label": "ALIRAN FEE 30 HARI (SANKEY)", "blocks": [
      {"type": "sankey", "source": {"label": "Fee pengguna", "display": "±$1,30 juta"}, "flows": [
        {"label": "Aplikasi", "value": 1.16, "display": "±$1,16 juta · 89%", "color": "orange"},
        {"label": "Dibakar → holder", "value": 0.141, "display": "$141 ribu · 11%", "color": "green", "display_color": "green"}]},
      {"type": "note", "html": "Hanya fee; APT baru dari staking dihitung terpisah."}
    ], "label_color": "muted"},
    {"type": "card", "label": "DIBAKAR VS TOKEN BARU (12 BULAN KE DEPAN)", "blocks": [
      {"type": "bars", "label_width": 140, "rows": [
        {"label": "Dibakar (laju kini)", "value": 1.72, "color": "green", "display": "$1,72 juta"},
        {"label": "APT baru staking", "value": 14.8, "color": "orange", "display": "±$14,8 juta"},
        {"label": "Unlock komunitas &amp; yayasan", "value": 17.3, "color": "red", "display": "±$17,3 juta"}]},
      {"type": "note", "html": "Skala sama, pada harga $0,822. Unlock ±21 juta APT (Messari)."}
    ]}
  ]},
  {"type": "table", "mt": 10, "cols": "minmax(0px,1.25fr) 112px minmax(0px,1.3fr)", "header": ["TINGKAT", "NILAI", "CATATAN"], "rows": [
    ["1. Fee kotor jaringan", N("±$0,87 juta", "white", True, "laju kini $1,72 juta/th"), "12 bulan (est.): fee baru naik 10× sejak Maret"],
    ["2. Pendapatan protokol", N("±$0,87 juta", "white"), "100% fee dibakar; tidak ada bagian validator"],
    ["3. Pendapatan holder (DefiLlama)", N("$4.991/hari", "body", s="$1,82 juta disetahunkan"), "Chain revenue DefiLlama = fee yang dibakar"],
    [T("4. Nilai Diterima Holder"), N("±$0,87 juta", "white", True, "±1,15 juta APT (est.)"), "Pembakaran; dicek di dasbor suplai resmi Aptos"],
    [T("5. Hasil Bersih Holder"), N("−$16,4 juta", "red", True, "−2,3% MC"), "Nilai diterima − unlock ±21 juta APT × $0,822"]
  ], "hl": [3, 4], "align": ["l", "r", "l"]},
  {"type": "card", "label": "YANG PERLU DIINGAT PEMBACA", "blocks": [
    {"type": "ol", "items": [
      f"Holder APT {W('baru menerima ±$0,87 juta setahun')} lewat pembakaran, atau ±0,12% dari market cap.",
      "APT baru staking tidak dikurangkan (diterima staker), tetapi holder yang tidak men-stake tergerus ±2,6%/th."
    ]}
  ], "mt": 10}
]})

# ---------------- HAL 4: On-chain 1 ----------------
pages.append({"label": "On-chain 1", "subtitle": "Analisis on-chain (1/2): siapa memegang &amp; siapa yang bergerak", "blocks": [
  {"type": "bigsec", "num": "3", "title": "Analisis On-Chain", "mt": 16},
  {"type": "text", "html": f"Bagian ini membaca jejak di blockchain untuk menjawab: {W('siapa yang membeli, siapa yang menjual, dan apakah itu mendukung tesis?')} Data APT jauh lebih terbatas daripada BTC atau ETH; blok yang tidak punya data publik ditandai N/A.", "muted": True, "mb": 6},
  {"type": "sub", "num": "3.1", "title": "RINGKASAN SINYAL ON-CHAIN", "right": "data s.d. 21–22 Okt 2026"},
  {"type": "table", "cols": "140px 92px minmax(0px,1.4fr) minmax(0px,1fr)", "header": ["BLOK", "SINYAL", "ANGKA KUNCI", "ARTINYA"], "rows": [
    [T("Peta holder"), D("gold", "Campuran"), "±64% suplai di-stake; 326,7 juta belum terbuka, 210 juta di antaranya dikunci permanen", "Suplai yang siap dijual kecil, tetapi yayasan dominan"],
    [T("Jadwal unlock"), D("green", "Positif"), "Unlock tim/investor selesai 12 Okt; berikutnya ±1,75 juta/bln", "Unlock setahun turun ±85%"],
    [T("Dompet terbesar"), D("muted", "N/A"), "Daftar holder tidak tersedia di penjelajah publik", "Tidak bisa memverifikasi akumulasi"],
    [T("Arus bursa &amp; derivatif"), D("gold", "Netral"), "OI Binance $21,2 juta (−12,4%); funding 0,01%", "Kenaikan 21 Okt dari tutup posisi jual"],
    [T("Suplai bersih"), D("orange", "Waspada"), "Dibakar 174 ribu vs baru 1,5 juta APT per bulan", "Belum deflasi; masih +1,3%/th"],
    [T("Kualitas aktivitas"), D("orange", "Lemah"), "TVL $43,2 juta; stablecoin $949 juta (−51% dari puncak)", "Transaksi naik, nilai yang disimpan turun"]
  ], "align": ["l", "l", "l", "l"]},
  {"type": "note", "html": "Kesimpulan: dari sisi suplai, tekanan jual turun jelas setelah 12 Okt. Dari sisi permintaan, belum ada bukti pembeli baru: nilai yang disimpan di Aptos menyusut dan kenaikan harga terakhir ditopang penutupan posisi jual. Ini mendukung skenario Dasar, belum mendukung Optimis."},
  {"type": "sub", "num": "3.2", "title": "PETA HOLDER BERBASIS ENTITAS", "mt": 6, "right": "suplai total 1,21 miliar APT"},
  {"type": "image", "src": IMG("n_peta_q.png"), "alt": "Peta suplai APT dari batas 2,1 miliar sampai kunci 210 juta", "plate": "none", "mt": 2},
  {"type": "grid", "mt": 8, "cols": "minmax(0px,1fr) minmax(0px,1.1fr)", "items": [
    {"type": "card", "label": "IMBALAN STAKING DARI WAKTU KE WAKTU", "blocks": [
      {"type": "bars", "label_width": 150, "max": 7.5, "rows": [
        {"label": "Rancangan awal", "value": 7, "color": "muted", "display": "±7%"},
        {"label": "Setelah AIP-119", "value": 5.19, "color": "orange", "display": "5,19%"},
        {"label": "Sejak Mar 2026", "value": 2.6, "color": "green", "display": "2,6%"}]},
      {"type": "note", "html": "Everstake, Aptos Foundation. Imbalan turun, APT baru ikut turun."}
    ]},
    {"type": "card", "label": "PENJAGA JARINGAN", "blocks": [
      {"type": "kv", "rows": [
        ["Validator", "149"],
        ["Nakamoto coefficient", "18"],
        ["Di-stake ÷ suplai total", "±64%"],
        ["Suara proposal batas suplai", "335,2 juta setuju · ±1.500 tolak"]]},
      {"type": "note", "html": "Chainspect (data bisa tertinggal) dan Everstake. Konsensus cukup tersebar, tetapi suara tata kelola didominasi stake terkait yayasan."}
    ]}
  ]}
]})

# ---------------- HAL 5: On-chain 2 ----------------
pages.append({"label": "On-chain 2", "subtitle": "Analisis on-chain (2/2): dompet, arus bursa &amp; kualitas aktivitas", "blocks": [
  {"type": "sub", "num": "3.3", "title": "DOMPET TERBESAR &amp; DOMPET BESAR BARU", "mt": 18},
  {"type": "text", "html": "N/A — tidak tersedia publik. Penjelajah resmi Aptos menampilkan “No Data Found” untuk daftar holder APT (21 Okt), dan Aptoscan akan ditutup 31 Okt 2026. Kami tidak memakai klaim “whale membeli” di media sosial yang tidak menyertakan alamat dompet. Satu-satunya holder besar yang bisa disebut dengan pasti adalah yayasan (210 juta APT dikunci).", "size": 10},
  {"type": "sub", "num": "3.5", "title": "ARUS BURSA &amp; PERMINTAAN SPOT VS DERIVATIF", "mt": 12},
  {"type": "table", "size": 9.5, "cols": "minmax(0px,1.3fr) 104px 104px minmax(0px,1.4fr)", "header": ["UKURAN", "KINI", "SEBELUMNYA", "ARTINYA"], "rows": [
    [T("Cadangan APT di bursa"), N("N/A", "muted"), N("N/A", "muted"), "Penyedia gratis tidak melacak APT"],
    [T("Open interest Binance"), N("$21,2 juta", s="21 Okt"), N("±$24,2 juta", "body", s="20 Okt (est.)"), "Turun 12,4% saat harga naik 9,7%: posisi jual ditutup"],
    [T("Funding rate"), N("0,01%/8 jam", "body"), N("—", "muted"), "Netral; tidak ada desakan beli dengan leverage"],
    [T("Volume spot bursa terpusat"), N("$75,2 juta", "body", s="24 jam"), N("$58,6 juta", "body", s="CMC"), "Likuid: 8–10% market cap per hari"],
    [T("Volume DEX di Aptos"), N("$5,5 juta", "body", s="24 jam"), N("$39,5 juta", "body", s="7 hari"), "Kecil; turun 9,8% seminggu"],
    [T("Volume perpetual di Aptos"), N("$53,6 juta", "white", s="24 jam"), N("$396,6 juta", "body", s="7 hari"), "Naik 18,4% seminggu; motor aktivitas utama"],
    [T("Setoran dompet tim/investor ke bursa"), N("N/A", "muted"), N("N/A", "muted"), "Tidak ada data dompet yang terverifikasi"]
  ], "align": ["l", "r", "r", "l"]},
  {"type": "note", "html": "Angka open interest dan volume tidak dibandingkan antar-penyedia. OI 20 Okt dihitung mundur dari perubahan −12,4% (est.)."},
  {"type": "sub", "num": "3.7", "title": "KUALITAS AKTIVITAS JARINGAN", "mt": 12, "right": "DefiLlama · dasbor Aptos · 21 Okt"},
  {"type": "table", "size": 9.5, "cols": "minmax(0px,1.2fr) 120px minmax(0px,1.6fr)", "header": ["UKURAN", "KINI", "ARTINYA"], "rows": [
    [T("Transaksi per hari"), N("9,7–14,35 juta", "body", s="dasbor Aptos / DefiLlama"), "Naik dari ±3,1 juta (Okt 2025); 98% dari order book Decibel (Messari)"],
    [T("Fee rata-rata"), N("±$0,0005", "body"), "Sangat murah, bahkan setelah naik 10×"],
    [T("Fee jaringan vs APT baru"), N("±11%", s="dibakar ÷ staking"), "Keamanan masih dibayar dengan mencetak APT"],
    [T("Insentif token aplikasi"), N("$0", s="DefiLlama"), "Aktivitas tidak disubsidi token secara langsung"],
    [T("TVL DeFi"), N("$43,2 juta", "red", s="−94% vs Okt 2025"), "Jauh di bawah ±$710 juta (Okt 2025, Everstake; definisi bisa berbeda)"],
    [T("Stablecoin"), N("$948,98 juta", s="+4,75% 7 hari"), "Turun dari puncak $1,95 miliar (Mei 2026)"],
    [T("Alamat aktif 24 jam"), N("30.831", "muted", s="definisi DefiLlama"), "Hanya untuk tren; tidak sebanding dengan angka sumber lain"]
  ], "align": ["l", "r", "l"]},
  {"type": "sub", "num": "3.8", "title": "DARI ON-CHAIN KE TESIS · YANG DIPANTAU", "mt": 12},
  {"type": "table", "size": 9.5, "cols": "minmax(0px,1.5fr) 110px minmax(0px,1.35fr) 58px", "header": ["INDIKATOR ON-CHAIN", "KINI", "TARGET / BATAS WASPADA", "TERKAIT"], "rows": [
    ["Suplai beredar (CMC)", "883,3 juta", "≤915 juta pada 22 Okt 2027", "P1"],
    ["APT dibakar per 30 hari", "174 ribu", "≥500 ribu (Sep 2027)", "P2"],
    ["Stablecoin di Aptos", "$949 juta", "≥$1,5 miliar · waspada &lt;$700 juta", "P3 · R1"],
    ["TVL DeFi Aptos", "$43,2 juta", "waspada &lt;$30 juta", "R1"],
    ["Volume perpetual Decibel 7 hari", "$396,6 juta", "naik · waspada turun 3 minggu", "P2"],
    ["Open interest Binance", "$21,2 juta", "waspada naik cepat tanpa volume spot", "R1"]
  ], "align": ["l", "r", "l", "r"]}
]})

# ---------------- HAL 6: Pendorong ringkasan + 4.1 ----------------
pages.append({"label": "Detail pendorong - ringkasan", "subtitle": "Detail pendorong (1/6): ringkasan &amp; peta suplai", "blocks": [
  {"type": "bigsec", "num": "4", "title": "Detail Pendorong"},
  {"type": "grid", "cols": "repeat(3, minmax(0px,1fr))", "gap": 10, "items": [
    {"type": "card", "label": "P1 · UTAMA · 70%", "blocks": [
      {"type": "text", "html": W("Unlock tim &amp; investor selesai")},
      {"type": "text", "html": "Ukuran: suplai beredar ≤915 juta APT (22 Okt 2027)", "size": 9.5, "muted": True}], "accent": "green"},
    {"type": "card", "label": "P2 · SUPLAI · 25%", "blocks": [
      {"type": "text", "html": W("Pembakaran fee naik 3×")},
      {"type": "text", "html": "Ukuran: dibakar ≥500 ribu APT per 30 hari (30 Sep 2027)", "size": 9.5, "muted": True}], "accent": "gold"},
    {"type": "card", "label": "P3 · PERMINTAAN · 35%", "blocks": [
      {"type": "text", "html": W("Stablecoin kembali tumbuh")},
      {"type": "text", "html": "Ukuran: stablecoin di Aptos ≥$1,5 miliar (30 Jun 2027)", "size": 9.5, "muted": True}], "accent": "info"}
  ]},
  {"type": "sub", "num": "4.1", "title": "“MENUJU DEFLASI”: DI MANA POSISI APT SEKARANG", "mt": 12, "right": "dasbor suplai Aptos · 21 Okt 2026"},
  {"type": "text", "html": "Suplai APT bertambah dari dua keran dan berkurang dari satu saluran. Keran pertama adalah unlock: token lama yang terkunci dilepas ke pasar. Keran kedua adalah staking: APT baru dicetak untuk staker. Salurannya adalah pembakaran fee. Deflasi baru terjadi bila saluran lebih besar dari keran."},
  {"type": "steps", "mt": 8, "items": [
    {"title": "Maret 2026: aturan diubah", "text": "Batas 2,1 miliar, imbalan staking 5,19% → 2,6%, gas naik 10× dan semua dibakar.", "color": "muted"},
    {"title": "12 Okt 2026: unlock orang dalam habis", "text": "Unlock bulanan turun dari 11,31 juta ke ±1,75 juta APT.", "color": "info"},
    {"title": "Kini: masih inflasi", "text": "Dibakar ±174 ribu, dicetak ±1,5 juta APT per bulan. Suplai bersih +1,3% per tahun.", "color": "gold"},
    {"title": "Titik impas", "text": "Butuh ±91 juta transaksi per hari, ±9× lipat dari sekarang (Tokenpost).", "color": "green"}
  ]},
  {"type": "image", "src": IMG("c_unlock_q.png"), "alt": "Unlock APT per 12 bulan 2023–2032", "plate": "none", "mt": 10},
  {"type": "text", "html": f"{W('Tekanan jual terbesar sudah lewat.')} Token yang masuk pasar kini ±3,3 juta per bulan (unlock + APT baru staking), dari ±12,8 juta sebelumnya. Pertanyaannya bukan lagi kapan unlock selesai, tetapi apakah ada permintaan baru.", "size": 10, "mt": 6},
  {"type": "table", "size": 9.5, "mt": 10, "cols": "minmax(0px,1.3fr) 110px 110px minmax(0px,1fr)", "header": ["UKURAN", "SEBELUM", "SESUDAH", "SUMBER"], "rows": [
    [T("Imbalan staking"), N("5,19%/th"), N("2,6%/th"), "AIP, Mar 2026"],
    [T("Harga gas"), N("1×"), N("10×"), "AIP, Mar 2026"],
    [T("Dibakar ÷ APT baru"), N("±0,2%"), N("±11%"), "Tokenpost, 20 Okt"],
    [T("Suplai bersih per tahun"), N("±5%"), N("±1,5%"), "Blockworks via Tokenpost/CMC"],
    [T("Batas suplai"), N("tidak ada"), N("2,1 miliar"), "Proposal #183"],
    [T("Unlock per bulan"), N("11,31 juta"), N("±1,75 juta"), "Messari (media: 4,54 juta)"],
    [T("Dikunci permanen yayasan"), N("0"), N("210 juta"), "Aptos Foundation"]
  ], "align": ["l", "r", "r", "l"]},
  {"type": "text", "html": "Hampir semua ukuran membaik setelah Maret. Transaksi juga berlipat dua (±4,5 → 9–10 juta per hari) walau gas 10× lebih mahal, tetapi 98% di antaranya berasal dari satu aplikasi: Decibel.", "size": 9.5, "muted": True, "mt": 6},
  {"type": "card", "label": "CATATAN DATA", "mt": 10, "blocks": [
    {"type": "text", "html": "Sebagian data di bagian ini berasal dari Blockworks Research (Okt 2026), riset yang dibiayai Aptos Foundation. Angkanya kami cek silang dengan dasbor suplai resmi Aptos, DefiLlama, dan Tokenpost (20 Okt), lalu kami hitung ulang sendiri.", "size": 9.5}
  ]}
]})


# ---------------- HAL BARU: Batas suplai ----------------
pages.append({"label": "Detail pendorong - batas suplai", "subtitle": "Detail pendorong (2/6): batas suplai 2,1 miliar", "blocks": [
  {"type": "sub", "num": "4.2", "title": "BATAS SUPLAI 2,1 MILIAR APT: APA ARTINYA BAGI HOLDER", "mt": 16, "right": "Proposal #183 · disahkan 1 Mar 2026"},
  {"type": "text", "html": f"Selama 3,5 tahun pertama, APT tidak punya batas suplai: staking boleh mencetak APT baru tanpa ujung. Pada 1 Mar 2026 holder yang men-stake menyetujui {W('batas maksimum 2,1 miliar APT')} di tingkat protokol. Hasil suaranya 335,2 juta APT setuju dan ±1.500 menolak (99,99%) dengan partisipasi 39%. APT masih jauh dari batasnya, dan batas itu bisa diubah lagi lewat tata kelola."},
  {"type": "image", "src": IMG("c_proyeksi_q.png"), "alt": "Proyeksi suplai APT menuju batas 2,1 miliar", "plate": "none", "mt": 8},
  {"type": "grid", "mt": 6, "cols": "repeat(4, minmax(0px,1fr))", "gap": 8, "items": [
    {"type": "kv", "rows": [["Sudah ada", "57,6% batas"]]},
    {"type": "kv", "rows": [["Ruang cetak", "±890 juta"]]},
    {"type": "kv", "rows": [["FDV di batas", "$1,73 miliar"]]},
    {"type": "kv", "rows": [["Dilusi maks.", "−42,4%", "red"]]}]},
  {"type": "sub", "num": "", "title": "BATAS SUPLAI DI JARINGAN LAIN", "mt": 12},
  {"type": "table", "size": 9.5, "cols": "minmax(0px,1fr) 104px 104px minmax(0px,1.6fr)", "header": ["JARINGAN", "BATAS", "SUDAH ADA", "CARA MEMBAYAR KEAMANAN"], "rows": [
    [T("Bitcoin (BTC)"), N("21 juta"), N("±95,7%", s="20,09 juta"), "Subsidi blok menyusut tiap 4 tahun; nanti hanya fee"],
    [T("Ethereum (ETH)", s="pemimpin kategori L1"), N("tidak ada"), N("—", "muted"), "Imbalan staking; inflasi bersih ±0,9%/th setelah pembakaran"],
    [T("Solana (SOL)"), N("tidak ada"), N("—", "muted"), "Inflasi turun bertahap ke 1,5%/th; 50% fee dibakar"],
    [T("Sui (SUI)"), N("10 miliar"), N("±41% beredar", s="FDV ÷ MC 2,43×"), "Imbalan dari cadangan yang sudah dicetak"],
    [T("Aptos (APT)"), N("2,1 miliar", "white", True), N("57,6%", "white", True, "beredar 42,1%"), "Imbalan 2,6%/th dari APT baru; 100% fee dibakar"]
  ], "hl": [4], "align": ["l", "r", "r", "l"]},
  {"type": "note", "html": "BTC: on-chain 19 Okt. ETH: note Shariacrypto 1 Okt. SOL: BlockEden (Mar). SUI: DefiLlama 21 Okt."},
  {"type": "grid", "mt": 10, "cols": "minmax(0px,1fr) minmax(0px,1fr)", "align": "start", "items": [
    {"type": "card", "label": "YANG BERUBAH KARENA BATAS INI", "blocks": [{"type": "ul", "items": [
      f"{W('Dilusi kini ada ujungnya.')} Holder yang tidak men-stake paling banyak tergerus ±42%, bukan tanpa batas seperti sebelum Maret.",
      f"{W('FDV punya angka pasti.')} Pada harga kini, nilai seluruh APT di batas maksimum ±$1,73 miliar (2,38× market cap).",
      f"{W('Tekanan ke validator.')} Saat batas tercapai, imbalan tidak bisa lagi dicetak; validator harus hidup dari fee (KuCoin)."]}]},
    {"type": "card", "label": "YANG TIDAK BERUBAH", "blocks": [{"type": "ul", "items": [
      f"{W('Suplai 12 bulan ke depan.')} Batas baru “menggigit” puluhan tahun lagi. Yang menentukan suplai setahun ke depan adalah imbalan 2,6% dan unlock ±1,75 juta per bulan.",
      f"{W('Harga belum merespons.')} Sejak suara disahkan (1 Mar), APT −11% sementara BTC +26% (penutupan mingguan).",
      f"{W('Bisa diubah lagi.')} Batas ditetapkan lewat tata kelola dan bisa dinaikkan dengan cara yang sama (Risiko R2)."]}]}
  ]},
  {"type": "card", "label": "PENILAIAN KAMI", "mt": 10, "blocks": [
    {"type": "text", "html": f"Batas 2,1 miliar adalah {W('sinyal disiplin yang baik, tetapi belum mengikat')}. Ada dua hal yang belum dijelaskan secara publik: apakah APT yang dibakar membuka ruang cetak baru di bawah batas, dan dari mana imbalan validator dibayar bila fee tetap sekecil sekarang (fee jaringan hanya ±11% dari APT baru staking). Karena itu batas ini tidak kami beri alfa di skenario 12 bulan, dan skor “laju penambahan suplai” tetap dihitung dari inflasi nyata (±1,3–2,4%/th), bukan dari batasnya. Yang membuat batas ini bermakna bagi harga adalah P2: bila pembakaran menyamai APT baru, batas itu tidak akan pernah tercapai dan APT benar-benar menyusut.", "size": 10}
  ]}
]})



# ---------------- HAL: visual titik impas ----------------
pages.append({"label": "Detail pendorong - titik impas", "subtitle": "Detail pendorong (3/6): seberapa jauh dari deflasi", "blocks": [
  {"type": "sub", "num": "4.3", "title": "SEBERAPA JAUH APT DARI DEFLASI", "mt": 16, "right": "data s.d. 27 Sep 2026"},
  {"type": "text", "html": f"Setiap transaksi di Aptos membakar rata-rata ±0,00058 APT, sementara staking mencetak ±19,4 juta APT per tahun. Dari dua angka itu kita bisa menghitung berapa transaksi yang dibutuhkan agar suplai berhenti bertambah: {W('±91 juta per hari, sekitar 10× hari ini')}. Sebelum Maret, dengan imbalan 5,19% dan gas sepersepuluhnya, titik itu ada di ±2 miliar transaksi per hari, praktis mustahil."},
  {"type": "image", "src": IMG("n_impas_q.png"), "alt": "Kurva suplai bersih APT terhadap transaksi per hari", "plate": "none", "mt": 8},
  {"type": "grid", "mt": 10, "cols": "repeat(3, minmax(0px,1fr))", "gap": 10, "items": [
    {"type": "card", "label": "LABA BERSIH HOLDER", "blocks": [{"type": "text", "html": "Fee yang dibakar kini sedikit lebih besar dari komisi validator: ±$20–30 ribu vs ±$17–25 ribu per minggu (Agu–Sep). Positif sejak Mei, tetapi tipis dan turun dari puncak ±$42 ribu per minggu.", "size": 9.5}]},
    {"type": "card", "label": "KEAMANAN TETAP TERJAGA", "blocks": [{"type": "text", "html": "Imbalan staking dipotong separuh, tetapi APT yang di-stake hanya turun ±10% sejak Februari. ±64% suplai masih di-stake, salah satu yang tertinggi di antara L1 besar.", "size": 9.5}]},
    {"type": "card", "label": "PENYERAP SUPLAI TERSEMBUNYI", "blocks": [{"type": "text", "html": "Setiap akun dan posisi baru mengunci deposit penyimpanan. ±457 ribu APT kini tertahan; hanya 14% yang pernah ditarik. Kecil, tetapi tumbuh bersama pemakaian.", "size": 9.5}]}
  ]},
  {"type": "image", "src": IMG("n_aptbtc_q.png"), "alt": "Harga APT dan BTC 52 minggu, disamakan ke 100", "plate": "none", "mt": 10, "caption": "Aturan Maret belum menahan penurunan; selisih terbesar terjadi saat unlock 11,31 juta APT per bulan masih berjalan."}
]})

# ---------------- HAL 7: P1 ----------------
pages.append({"label": "Detail pendorong 1", "subtitle": "Detail pendorong (4/6)", "blocks": [
  {"type": "spacer", "h": 4},
  {"type": "dcard", "tag": "PENDORONG 01 — UTAMA · DAMPAK PALING BESAR", "title": "Unlock tim &amp; investor awal selesai", "subtitle": "Penjual tetap yang selama empat tahun menekan harga kini hilang", "pills": [{"t": "Okt 2026–Okt 2027", "c": "warning"}, {"t": "PELUANG 70%", "c": "green"}], "accent": "green", "rows": [
    {"label": "MEKANISME", "blocks": [
      {"type": "ol", "items": [
        f"{W('Penjual tetap berkurang.')} Sejak 2023 kontributor inti dan investor awal menerima ±6,77 juta APT tiap bulan. Sebagian besar dijual untuk menutup biaya atau mengambil untung. Mulai 12 Okt 2026 aliran ini berhenti.",
        f"{W('Laju suplai beredar melambat.')} Suplai beredar naik ±135,7 juta APT sepanjang 2026 (±15%). Setahun ke depan tinggal ±21 juta (±2,4%) menurut Messari, plus APT baru staking yang sebagian besar diterima staker.",
        f"{W('Pasar lebih mudah menyerap.')} Dengan volume harian ±$75 juta, sisa unlock ±$47 ribu per hari hampir tidak terasa."
      ]},
      {"type": "note", "html": "Kebocoran: di luar 210 juta yang dikunci, yayasan dan komunitas masih memegang ±117–125 juta APT yang belum terbuka dan bisa mempercepat hibah lewat tata kelola. Unlock berakhir bukan berarti ada pembeli baru; dampaknya hanya mengurangi penjual."}
    ]},
    {"label": "DAMPAK TERUKUR", "blocks": [
      {"type": "text", "html": f"{W('Ilustrasi sederhana:')} sampai September, pasar harus menyerap ±377 ribu APT baru setiap hari dari unlock, senilai ±$310 ribu. Mulai Oktober tinggal ±57 ribu APT per hari. Bandingkan dengan APT yang dibakar: hanya ±5.800 per hari."},
      {"type": "bars", "label_width": 210, "max": 400, "rows": [
        {"label": "Unlock per hari s.d. Sep 2026", "value": 377, "color": "red", "display": "±377 ribu APT"},
        {"label": "Unlock per hari mulai Okt 2026", "value": 57.5, "color": "orange", "display": "±57 ribu APT"},
        {"label": "APT baru staking per hari", "value": 50, "color": "gold", "display": "±50 ribu APT"},
        {"label": "APT dibakar per hari", "value": 5.8, "color": "green", "display": "±5.800 APT"}]},
      {"type": "mtab", "cols": "minmax(0px,1.4fr) 84px 96px minmax(0px,1.1fr)", "hl": 2, "header": ["UKURAN", "KINI", "12 BLN LAGI*", "SUMBER DATA"], "rows": [
        ["Unlock per bulan", "±1,75 juta", "±1,75 juta", "Messari (media: 4,54 juta)"],
        ["Suplai beredar", "883,3 juta", "≤915 juta", "CoinMarketCap"],
        ["Kenaikan suplai beredar 12 bln", "±15% (2026)", "±2–4%", "hitungan sendiri"],
        ["APT baru bersih (staking − dibakar)", "±1,33 juta/bln", "≤1,5 juta/bln", "dasbor suplai Aptos"]]},
      {"type": "formula", "html": "Alfa +5 poin di skenario Dasar (P1): $0,822 × (1 + 1,32 × 21,3% + 5%) = $1,095<br>Alasan: APT turun 77% setahun saat BTC turun 28%; sebagian selisih itu berasal dari unlock yang kini selesai."},
      {"type": "note", "html": "*ESTIMASI. Messari dan Tokenpost: unlock ±21 juta per tahun. Media lain menulis 4,54 juta per bulan, tetapi angka itu tidak cocok dengan sisa ±332 juta yang belum terbuka. Uji pertama 12 Nov: suplai beredar naik ±1,75 juta atau ±4,54 juta."}
    ]},
    {"label": "INDIKATOR PANTAU", "blocks": [{"type": "text", "html": f"{W('Bulanan:')} suplai beredar CMC (naik ≤±2,5 juta per bulan) · unlock tanggal 12 tiap bulan · proposal tata kelola yang mengubah jadwal hibah · selisih kinerja APT vs BTC."}]},
    {"label": "PEMICU &amp; WAKTU", "blocks": [{"type": "text", "html": "Sudah berlaku sejak 12 Okt 2026. Dampaknya terlihat bertahap selama 3–12 bulan, saat pasar sadar tidak ada lagi penjual tetap dari tim dan investor."}]},
    {"label": "SUMBER IDE", "blocks": [{"type": "text", "html": "Everstake (jadwal unlock, 30 Sep 2026); Aptos Foundation (pembaruan tokenomics, 18 Feb 2026); KuCoin Research (10 Okt 2026); permintaan pemilik setelah membaca laporan Messari."}]},
    {"label": "PELUANG &amp; KEYAKINAN", "blocks": [{"type": "text", "html": f"{W('70%')}: suplai beredar APT (CoinMarketCap) ≤915 juta pada 22 Okt 2027. {W('Keyakinan: sedang')}: jadwal tertulis di kontrak, tetapi dua sumber masih berbeda soal laju unlock. Sisa 30% untuk hibah dipercepat, versi media yang benar, atau perubahan cara CMC menghitung suplai beredar."}]}
  ], "mt": 8},
  {"type": "note", "html": "Dalam 52 minggu (20 Okt 2025 sampai 19 Okt 2026), APT turun 77% saat BTC turun 28%. Dengan beta 1,32, APT seharusnya hanya turun ±36%. Selisih ±41 poin sebagian besar terjadi saat unlock 11,31 juta APT per bulan masih berjalan (grafik di 4.3). Itu sebabnya P1 diberi alfa di skenario Dasar. Bila suplai beredar pada 12 Nov naik jauh di atas ±1,75 juta, alfa ini perlu ditinjau ulang.", "mt": 20}
]})

# ---------------- HAL 8: P2 ----------------
pages.append({"label": "Detail pendorong 2", "subtitle": "Detail pendorong (5/6)", "blocks": [
  {"type": "dcard", "tag": "PENDORONG 02 — SUPLAI · PEMBAKARAN", "title": "Pembakaran fee naik tiga kali lipat", "subtitle": "Decibel dan aplikasi trading menambah transaksi; setiap transaksi membakar APT", "pills": [{"t": "s.d. 30 Sep 2027", "c": "warning"}, {"t": "PELUANG 25%", "c": "gold"}], "accent": "gold", "mt": 8, "rows": [
    {"label": "MEKANISME", "blocks": [
      {"type": "ol", "items": [
        "Setiap transaksi di Aptos membayar gas dengan APT, dan seluruhnya dibakar.",
        "Decibel, bursa perpetual dengan order book di blockchain, membuat satu transaksi untuk setiap order, pembatalan, dan penyelesaian. Makin ramai, makin banyak APT dibakar.",
        "Bila pembakaran menyamai APT baru dari staking (±1,5 juta per bulan), suplai berhenti naik."
      ]},
      {"type": "note", "html": "Kebocoran: fee per transaksi sangat murah (±$0,0005). Kenaikan volume dalam dolar tidak otomatis menaikkan pembakaran; yang dihitung adalah jumlah transaksi dan harga gas. Fee perpetual (±$559 ribu per 30 hari) masuk ke Decibel, bukan ke holder APT."}
    ]},
    {"label": "DAMPAK TERUKUR", "blocks": [
      {"type": "text", "html": f"{W('Ilustrasi sederhana:')} agar APT benar-benar menyusut, yang dibakar harus menyamai ±1,5 juta APT baru dari staking setiap bulan. Sekarang baru ±174 ribu, kira-kira sepersembilannya. Target P2 adalah ±500 ribu per bulan: tiga kali lipat, tetapi masih sepertiga jalan menuju impas."},
      {"type": "bars", "label_width": 230, "max": 2800, "rows": [
        {"label": "Dibakar per bulan kini", "value": 174, "color": "green", "display": "±174 ribu APT"},
        {"label": "Target P2", "value": 500, "color": "gold", "display": "≥500 ribu APT"},
        {"label": "APT baru dari staking", "value": 1500, "color": "orange", "display": "±1,5 juta APT"},
        {"label": "Klaim yayasan: Decibel 100+ pasar", "value": 2667, "color": "info", "display": "±2,7 juta APT"}]},
      {"type": "mtab", "cols": "minmax(0px,1.4fr) 84px 96px minmax(0px,1.1fr)", "hl": 2, "header": ["UKURAN", "KINI", "12 BLN LAGI*", "SUMBER DATA"], "rows": [
        ["APT dibakar per 30 hari", "174.210", "≥500 ribu", "dasbor suplai Aptos"],
        ["Transaksi per hari", "9,7 juta", "±28 juta", "dasbor Aptos"],
        ["Volume perpetual 7 hari", "$396,6 juta", "≥$1 miliar", "DefiLlama"],
        ["Dibakar ÷ APT baru staking", "±11%", "±33%", "hitungan sendiri"]]},
      {"type": "formula", "html": "Alfa +10 poin di skenario Optimis (P2): $0,822 × (1 + 1,32 × 57,7% + 10%) = $1,531<br>Pembakaran ±6 juta APT per tahun × $1,53 = ±$9 juta → lama balik modal ±160 tahun pada MC $1,44 miliar"},
      {"type": "note", "html": "*ESTIMASI. Klaim &gt;32 juta APT per tahun dari yayasan (Feb 2026) berlaku bila Decibel punya 100+ pasar; belum ada tanggalnya."}
    ]},
    {"label": "INDIKATOR PANTAU", "blocks": [{"type": "text", "html": "Dibakar 30 hari di dasbor suplai Aptos · transaksi harian · volume dan jumlah pasar Decibel · usulan kenaikan harga gas berikutnya."}]},
    {"label": "PEMICU &amp; WAKTU", "blocks": [{"type": "text", "html": "Peluncuran pasar baru di Decibel, Block-STM v2 jadi jalur eksekusi utama (Okt 2026), dan kenaikan gas lanjutan yang sudah disebut yayasan sebagai opsi."}]},
    {"label": "SUMBER IDE", "blocks": [{"type": "text", "html": "Aptos Foundation (18 Feb 2026); dasbor suplai Aptos (21 Okt); Tokenpost (20 Okt); The Block (peluncuran Decibel)."}]},
    {"label": "PELUANG &amp; KEYAKINAN", "blocks": [{"type": "text", "html": f"{W('25%')}: APT dibakar ≥500 ribu per 30 hari pada 30 Sep 2027. {W('Keyakinan: rendah')}. Pembakaran naik ±14× dalam dolar karena gas 10× dan transaksi 2×, tetapi 98% transaksi datang dari satu aplikasi."}]}
  ]},
  {"type": "card", "label": "BERAPA TRANSAKSI PER HARI UNTUK MENCAPAI TARGET", "mt": 8, "blocks": [
    {"type": "bars", "label_width": 230, "max": 120, "rows": [
      {"label": "Aptos kini (dasbor Aptos)", "value": 9.7, "color": "green", "display": "9,7 juta"},
      {"label": "Target P2 (≥500 ribu APT dibakar)", "value": 28, "color": "gold", "display": "±28 juta"},
      {"label": "Impas: dibakar = APT baru", "value": 91, "color": "orange", "display": "±91 juta"},
      {"label": "Solana kini (DefiLlama)", "value": 115.4, "color": "muted", "display": "115,4 juta"}]},
    {"type": "note", "html": "Dengan fee rata-rata tetap ±$0,0005. Solana sebagai pembanding skala: jaringan tersibuk pun hanya ±1,3× titik impas Aptos. Cara lain mencapai target adalah menaikkan harga gas lagi."}
  ]}
]})

# ---------------- HAL 9: P3 + tree ----------------
pages.append({"label": "Detail pendorong 3", "subtitle": "Detail pendorong (6/6)", "blocks": [
  {"type": "dcard", "tag": "PENDORONG 03 — PENDUKUNG · PERMINTAAN", "title": "Stablecoin &amp; pembayaran kembali tumbuh", "subtitle": "Aptos sebagai jalur kirim dolar digital yang murah", "pills": [{"t": "s.d. 30 Jun 2027", "c": "warning"}, {"t": "PELUANG 35%", "c": "info"}], "accent": "info", "mt": 8, "rows": [
    {"label": "MEKANISME", "blocks": [{"type": "text", "html": "Mitra pembayaran (Yellow Card, Bitso, coins.ph) memakai Aptos untuk transfer USDT dan USDC. Makin banyak dolar digital yang berpindah, makin banyak APT yang dibakar. Kebocorannya: biaya transfer stablecoin ±$0,00014, jadi butuh volume yang sangat besar agar terasa di pembakaran."}]},
    {"label": "DAMPAK TERUKUR", "blocks": [
      {"type": "text", "html": f"{W('Ilustrasi sederhana:')} pada Mei 2026 ada $1,95 miliar stablecoin di Aptos. Kini tinggal $949 juta, kira-kira separuhnya. P3 tercapai bila stablecoin kembali ke $1,5 miliar, sekitar tiga perempat jalan menuju puncak."},
      {"type": "bars", "label_width": 200, "max": 2000, "rows": [
        {"label": "Puncak Mei 2026", "value": 1950, "color": "muted", "display": "$1,95 miliar"},
        {"label": "Target P3", "value": 1500, "color": "info", "display": "$1,5 miliar"},
        {"label": "Kini (21 Okt)", "value": 949, "color": "orange", "display": "$949 juta"}]},
      {"type": "mtab", "cols": "minmax(0px,1.4fr) 84px 96px minmax(0px,1.1fr)", "hl": 2, "header": ["UKURAN", "KINI", "12 BLN LAGI*", "SUMBER DATA"], "rows": [
        ["Stablecoin di Aptos", "$949 juta", "≥$1,5 miliar", "DefiLlama"],
        ["Porsi USDT", "49,2%", "—", "DefiLlama"],
        ["RWA aktif", "$761 juta", "≥$900 juta", "DefiLlama RWA"]]},
      {"type": "note", "html": "*ESTIMASI. P3 tidak diberi alfa karena dampaknya ke pembakaran kecil; pengaruhnya ke harga lewat sentimen ekosistem."}
    ]},
    {"label": "PELUANG &amp; KEYAKINAN", "blocks": [{"type": "text", "html": f"{W('35%')}: stablecoin di Aptos ≥$1,5 miliar pada 30 Jun 2027 (DefiLlama). {W('Keyakinan: rendah')}; naik 4,75% dalam seminggu terakhir, tetapi tren 5 bulan masih turun. Catatan syariah: sebagian besar RWA di Aptos berupa dana berbasis bunga (Bagian 7)."}]}
  ]},
  {"type": "sub", "num": "4.4", "title": "DARI PENDORONG KE SKENARIO &amp; JADWAL PEMANTAUAN", "mt": 12},
  {"type": "image", "src": IMG("c_kipas_q.png"), "alt": "Kipas skenario harga 12 bulan", "plate": "none", "mt": 4},
  {"type": "grid", "mt": 8, "align": "start", "cols": "minmax(0px,1fr) minmax(0px,1.1fr)", "items": [
    [{"type": "formula", "html": "Harga Perkiraan = 20%×1,531 + 55%×1,095 + 25%×0,445 = $1,019 (+24,0%)<br>Rasio Untung-Rugi = $0,291 ÷ $0,094 = 3,09×"},
     {"type": "card", "mt": 8, "label": "YANG TIDAK MASUK SKENARIO", "blocks": [
    {"type": "text", "html": "P3 (stablecoin), R2 (tata kelola), dan R3 (gangguan jaringan) tidak diberi alfa. Dampaknya ke harga sulit diukur dan peluangnya di bawah 40%. Ketiganya dipantau di Dasbor 7.2. Bila salah satunya terjadi, note ini diperbarui lewat Update Kilat. Tidak ada Skenario Khusus: tidak ada kejadian khusus APT dengan peluang ≥10% dan dampak ≥40% di luar skenario Pesimis.", "size": 9.5}
  ]}],
    {"type": "card", "label": "JADWAL &amp; TITIK UJI", "blocks": [
      {"type": "timeline", "rows": [
        ["12 Nov 2026", "Uji laju unlock: ±1,75 atau 4,54 juta", "P1"],
        ["28 Okt 2026", "Keputusan FOMC (Pandangan Pasar)", "Skenario"],
        ["Q4 2026", "Block-STM v2 jadi jalur utama; Confidential APT", "P2"],
        ["Bulanan", "Dibakar 30 hari · stablecoin · TVL", "P2 · P3 · R1"],
        ["30 Jun 2027", "Titik uji stablecoin ≥$1,5 miliar · TVL ≥$30 juta", "P3 · R1"],
        ["30 Sep 2027", "Titik uji dibakar ≥500 ribu APT/30 hari", "P2"],
        ["22 Okt 2027", "Titik uji suplai beredar ≤915 juta", "P1"]]}
    ]}
  ]}

]})

# ---------------- HAL 10: Valuasi ----------------
pages.append({"label": "Valuasi", "subtitle": "Valuasi vs pembanding", "blocks": [
  {"type": "bigsec", "num": "5", "title": "Valuasi vs Pembanding"},
  {"type": "text", "html": "Untuk L1, yang sampai ke holder adalah fee yang dibakar. Pembanding memakai data 24 jam × 365 (est.).", "mt": 0, "mb": 4},
  {"type": "table", "cols": "minmax(0px,0.9fr) 84px 80px 80px 86px 50px minmax(0px,1fr)", "header": ["PEMBANDING", "MARKET CAP", "DIBAKAR/TH", "BALIK MODAL", "TVL", "MC/TVL", "KETERANGAN"], "rows": [
    [T("Aptos (APT)"), N("$726,5 juta"), N("$1,72 juta", s="12 bln ±$0,87 juta"), N("±422 th", "white", True, "±840 th (12 bln)"), N("$43,2 juta"), N("16,8×", "white", True), "Batas suplai 2,1 miliar"],
    [T("Ethereum (ETH)", s="pemimpin kategori"), N("$306,6 miliar"), N("±$40,5 juta"), N("±7.570 th", "white", True), N("$50,6 miliar"), N("6,1×", "muted"), "Pembakaran base fee"],
    [T("Solana (SOL)"), N("$63,5 miliar"), N("±$42,7 juta"), N("±1.490 th", "white", True), N("$6,03 miliar"), N("10,5×", "muted"), "Pesaing aktivitas"],
    [T("NEAR"), N("$7,00 miliar"), N("±$1,06 juta"), N("±6.620 th", "white", True), N("$248,2 juta"), N("28,2×", "muted"), "L1 serupa (note 19 Okt)"],
    [T("Sui (SUI)"), N("$4,30 miliar"), N("±$9 ribu"), N("&gt;100.000 th", "white", True), N("$515,8 juta"), N("8,3×", "muted"), "Pesaing langsung"]
  ], "hl": [0], "align": ["l", "r", "r", "r", "r", "r", "l"]},
  {"type": "image", "src": IMG("c_valuasi_q.png"), "alt": "Market cap vs pendapatan holder L1, skala log", "plate": "none", "mt": 8, "caption": "Lensa kedua: MC ÷ TVL APT 16,8×, lebih mahal dari SOL, SUI, dan ETH."},
  {"type": "sub", "num": "5.1", "title": "CEK KELIPATAN TARGET &amp; DUA LENSA", "mt": 9},
  {"type": "table", "size": 10.5, "cols": "92px 66px 86px minmax(0px,1fr) minmax(0px,1fr) minmax(0px,1.1fr)", "header": ["SKENARIO", "TARGET", "MC TERSIRAT", "BALIK MODAL ($1,72 JT)", "MC ÷ TVL ($43,2 JT)", "VS PEMIMPIN (ETH ±7.570 TH)"], "rows": [
    ["<span style=\"color: var(--success-solid); font-weight: 700;\">Optimis · 20%</span>", N("$1,531", "green", True), N("$1,44 miliar"), N("±834 th"), N("33×"), N("di bawah")],
    ["<span style=\"color: var(--info); font-weight: 700;\">Dasar · 55%</span>", N("$1,095", "info", True), N("$1,03 miliar"), N("±597 th"), N("24×"), N("di bawah")],
    ["<span style=\"color: var(--danger); font-weight: 700;\">Pesimis · 25%</span>", N("$0,445", "red", True), N("$417 juta"), N("±243 th"), N("9,7×"), N("di bawah")],
    ["<span style=\"color: var(--text-muted);\">Kini</span>", N("$0,822"), N("$726,5 juta"), N("±422 th"), N("16,8×"), ""]
  ], "align": ["l", "r", "r", "r", "r", "r"]},
  {"type": "grid", "mt": 8, "cols": "minmax(0px,1fr) minmax(0px,1.05fr)", "items": [
    {"type": "card", "label": "CARA MEMBACA", "blocks": [{"type": "text", "html": "Semua target masih di bawah kelipatan pemimpin kategori, jadi tidak ada target yang menuntut APT dinilai lebih mahal dari ETH. Harga Perkiraan +24% juga di bawah batas +30%. Yang perlu diwaspadai justru lensa TVL: target Dasar setara 24× TVL hari ini."}]},
    {"type": "card", "label": "HARGA TERSIRAT DARI DUA ANGKA", "blocks": [
      {"type": "heat", "corner": "DIBAKAR/TH ↓ · BALIK MODAL →", "col_labels": ["250 th", "420 th (kini)", "600 th"], "row_labels": ["$1,72 juta (kini)", "$2,5 juta", "$3,5 juta", "$5 juta (P2)"], "values": [[0.459, 0.770, 1.100], [0.667, 1.120, 1.600], [0.933, 1.568, 2.239], [1.333, 2.239, 3.199]], "thresholds": [0.822, 1.095], "decimals": 3},
      {"type": "note", "html": "Harga = dibakar per tahun × kelipatan ÷ ±938 juta APT. Merah: di bawah harga kini · kuning: di bawah target Dasar · hijau: di atasnya."}
    ]}
  ]},
  {"type": "sub", "num": "5.2", "title": "GAMBARAN JANGKA PANJANG 2030", "mt": 9, "right": "bukan target 12 bulan"},
  {"type": "text", "html": f"{W('Konservatif ±$0,70 · Moderat ±$1,57 · Optimis ±$3,91.')} Nilai pasar L1 2030 ($0,8/1,2/1,8 triliun) × porsi Aptos (0,10/0,15/0,25%) ÷ ±1,15 miliar APT (est.).", "size": 10}
]})

# ---------------- HAL 11: Risiko ----------------
pages.append({"label": "Risiko", "subtitle": "Yang bisa mematahkan tesis", "blocks": [
  {"type": "bigsec", "num": "6", "title": "Yang Bisa Mematahkan Tesis", "mt": 14},
  {"type": "dcard", "tag": "RISIKO 01 — PALING BERBAHAYA", "title": "Ekosistem terus mengecil &amp; kalah bersaing", "title_size": 13, "pills": [{"t": "PELUANG 30% · ALFA PESIMIS", "c": "red"}], "accent": "red", "mt": 7, "rows": [
    {"label": "MEKANISME", "blocks": [{"type": "ol", "items": [
      "98% transaksi, dan hampir semua pembakaran, berasal dari Decibel. Bila volumenya pindah ke pesaing, pembakaran ikut jatuh.",
      "Unlock selesai tidak berarti apa-apa bila tidak ada pembeli; APT turun lebih dalam dari BTC seperti setahun terakhir (−77% vs −28%)."]}]},
    {"label": "DAMPAK TERUKUR", "blocks": [{"type": "text", "html": "TVL DeFi $43,2 juta (21 Okt), dari ±$710 juta pada Okt 2025 (definisi bisa berbeda). Stablecoin $949 juta, −51% dari puncak. Masuk skenario sebagai alfa −10 poin di Pesimis: $0,822 × (1 − 1,32 × 27,2% − 10%) = $0,445."}]},
    {"label": "INDIKATOR PANTAU", "blocks": [{"type": "text", "html": "Volume Decibel 7 hari turun 3 minggu · TVL DeFi &lt;$30 juta · stablecoin &lt;$700 juta."}]},
    {"label": "PELUANG", "blocks": [{"type": "text", "html": f"{W('30%')}: TVL DeFi Aptos &lt;$30 juta dan stablecoin &lt;$700 juta pada 30 Jun 2027 (DefiLlama)."}]}
  ]},
  {"type": "dcard", "tag": "RISIKO 02 — DAMPAK SEDANG", "title": "Tata kelola berbalik arah", "title_size": 13, "pills": [{"t": "PELUANG 10%", "c": "gold"}], "accent": "gold", "mt": 7, "rows": [
    {"label": "MEKANISME", "blocks": [{"type": "ol", "items": [
      "Suara tata kelola didominasi stake yang terkait yayasan: proposal batas suplai lolos dengan 335,2 juta APT setuju dan hanya ±1.500 menolak.",
      "Bila staker mengeluh imbalan 2,6% terlalu kecil atau validator kekurangan biaya, imbalan bisa dinaikkan lagi, atau batas 2,1 miliar dinaikkan (Crypto Briefing menyebut batas ini “sementara”)."]}]},
    {"label": "DAMPAK TERUKUR", "blocks": [{"type": "text", "html": "Kembali ke 5,19% berarti APT baru dua kali lipat; narasi deflasi gugur."}]},
    {"label": "INDIKATOR PANTAU", "blocks": [{"type": "text", "html": "Proposal AIP baru tentang imbalan staking, harga gas, atau batas suplai · jumlah validator · porsi suara yayasan."}]},
    {"label": "PELUANG", "blocks": [{"type": "text", "html": f"{W('10%')}: proposal yang menaikkan imbalan staking di atas 2,6% atau batas suplai di atas 2,1 miliar disetujui sebelum 22 Okt 2027."}]}
  ]},
  {"type": "dcard", "tag": "RISIKO 03 — PERLU DIAWASI", "title": "Gangguan jaringan atau peretasan aplikasi besar", "title_size": 13, "pills": [{"t": "PELUANG 20%", "c": "muted"}], "accent": "muted", "mt": 7, "rows": [
    {"label": "MEKANISME", "blocks": [{"type": "text", "html": "Aptos pernah berhenti ±5 jam (19 Okt 2023) dan terganggu lagi pada Des 2024. Fitur baru (Block-STM v2, mempool terenkripsi, blok &lt;25 milidetik) menambah kerumitan. Peretasan di Decibel atau aplikasi pinjaman bisa menguras kepercayaan."}]},
    {"label": "DAMPAK TERUKUR", "blocks": [{"type": "text", "html": "Harga biasanya turun 10–20% dalam hitungan hari; dampak lebih panjang bila dana pengguna hilang."}]},
    {"label": "PELUANG", "blocks": [{"type": "text", "html": f"{W('20%')}: jaringan berhenti ≥2 jam atau peretasan ≥$10 juta di aplikasi Aptos sebelum 22 Okt 2027."}]}
  ]},
  {"type": "stats", "verdict": "HARGA MURAH · RASIO ±3,1×", "items": [
    {"label": "POTENSI NAIK", "value": "+$0,291", "color": "green", "sub": "20%×$0,708 + 55%×$0,272"},
    {"label": "POTENSI TURUN", "value": "−$0,094", "color": "red", "sub": "25% × $0,377"},
    {"label": "HARGA PERKIRAAN", "value": "$1,019", "color": "white", "sub": "+24,0% dari $0,822"},
    {"label": "RASIO UNTUNG-RUGI", "value": "3,09×", "color": "gold", "sub": "$0,291 ÷ $0,094"}
  ], "note": "Sikap: Beli Bertahap · keyakinan rendah. Dicicil 3–4 kali dalam beberapa bulan, porsi lebih besar di zona $0,73–0,78 (support terdekat) atau setelah suplai beredar dan pembakaran bergerak sesuai P1 dan P2. Keyakinan rendah karena hasil bersih holder masih negatif, ekosistem menyusut, dan sebagian besar Rasio Untung-Rugi berasal dari pandangan BTC, bukan dari APT sendiri.", "label": "RINGKASAN SKENARIO"}
]})

# ---------------- HAL 12: Syariah ----------------
pages.append({"label": "Catatan syariah", "subtitle": "Catatan syariah &amp; pemantauan", "disclaimer": "B", "blocks": [
  {"type": "bigsec", "num": "7", "title": "Catatan Syariah", "mt": 14},
  {"type": "sharia", "score": "74", "verdict": "Halal Bersyarat", "verdict_color": "warning", "summary": "DITAHAN menunggu Komite Syariah (porsi perpetual). Skor 74 (Halal Bersyarat 60–79). Beli dan simpan: Boleh. Staking: Bersyarat, imbalannya perlu tathir. Keyakinan rendah: porsi transaksi non-halal masih perkiraan kasar. Bukan fatwa.", "layers": [
    {"label": "LAPIS 1 · 26/30", "name": "Infrastruktur", "icon": "⚠️", "icon_color": "warning", "text": "Protokol intinya bersih (PoS, gas, tanpa bunga). Tetapi produk unggulan pengembang inti adalah bursa perpetual berleverage (Decibel).", "score": "26/30", "pct": 87},
    {"label": "LAPIS 2 · 28/30", "name": "Kegunaan token", "icon": "✅", "icon_color": "green", "text": "APT dipakai untuk gas ✅ dan staking ✅ (bagi hasil). Hak suara tata kelola ✅.", "score": "28/30", "pct": 93},
    {"label": "LAPIS 3 · 5/10", "name": "Sumber nilai", "icon": "⚠️", "icon_color": "warning", "text": "Perkiraan awal 15–30% fee dari perpetual dan dana berbunga. Data terbaru: 98% transaksi dari perpetual Decibel. Ditinjau Komite Syariah.", "score": "5/10", "pct": 50},
    {"label": "LAPIS 4 · 15/30", "name": "Penggunaan", "icon": "⚠️", "icon_color": "warning", "text": "Ada pemakaian riil (transfer stablecoin, pembayaran), tetapi fee aplikasi terbesar berasal dari tokenisasi dana berbunga dan perpetual.", "score": "15/30", "pct": 50}
  ], "after": [
    {"type": "card", "label": None, "blocks": [
      {"type": "text", "html": f"{W('Tathir:')} staker menyisihkan ±22,5% imbalan (perkiraan awal). Contoh: $1.000 → tathir ±$5,85/th. {W('Catatan:')} bila pembakaran hampir seluruhnya dari perpetual, Lapis 3 jatuh di bawah batas; status ditahan sampai Komite Syariah menetapkan."},
      {"type": "text", "html": f"{W('Pembanding:')} HalalScreener menilai APT “Halal”, skor 85/100 (21 Okt 2026). Lainnya N/A. Selisih karena HalalScreener tidak menilai sumber fee.", "muted": True, "mt": 3}
    ], "mt": 8},
    {"type": "table", "size": 9.5, "mt": 8, "cols": "minmax(0px,1fr) 92px minmax(0px,1.8fr)", "header": ["AKTIVITAS", "STATUS", "SYARAT / ALASAN"], "rows": [
      [T("Beli &amp; simpan"), D("green", "Boleh"), "Pertukaran aset nyata secara tunai"],
      [T("Staking"), D("gold", "Bersyarat"), "Langsung ke validator; tathir ±22,5% imbalan"],
      [T("Penyedia likuiditas"), D("gold", "Bersyarat"), "Hanya pool spot dengan pasangan halal"],
      [T("Pinjam-meminjam"), D("red", "Hindari"), "Mengandung riba (Echelon, Aries)"],
      [T("Perpetual / leverage"), D("red", "Hindari"), "Maysir dan riba (Decibel, futures bursa)"],
      [T("ETF / produk turunan"), D("gold", "Bersyarat"), "Hanya produk spot fisik; ETF APT belum terbit"]
    ], "align": ["l", "l", "l"]}
  ]},
  {"type": "image", "src": IMG("c_fee_q.png"), "alt": "Sumber fee aplikasi di Aptos 30 hari", "plate": "none", "mt": 8},
  {"type": "sub", "num": "7.1", "title": "DAMPAK PENDORONG &amp; RISIKO TERHADAP STATUS SYARIAH", "mt": 10},
  {"type": "table", "size": 9.5, "pad": 4, "cols": "130px minmax(0px,1.6fr) 90px", "header": ["PENDORONG / RISIKO", "PENGARUH KE SYARIAH", "ARAH SKOR"], "rows": [
        [T("P2 · Pembakaran naik"), "Pembakaran kini 98% dari Decibel (perpetual); Lapis 3 makin tertekan.", N("Lapis 3 turun", "red")],
    [T("P3 · Stablecoin"), "Transfer dan pembayaran stablecoin menambah penggunaan riil; Lapis 4 bisa naik.", N("Lapis 4 naik", "green")]
  ]}
]})

# ---------------- HAL 13: Dasbor ----------------
pages.append({"label": "Dasbor pantauan", "subtitle": "Dasbor pantauan", "disclaimer": "B", "blocks": [
  {"type": "sub", "num": "7.2", "title": "DASBOR PANTAUAN · CEK MINGGUAN/BULANAN", "mt": 18},
  {"type": "table", "size": 9.5, "cols": "minmax(0px,1.4fr) 120px minmax(0px,1.3fr) 64px", "header": ["INDIKATOR", "KINI", "TARGET / BATAS WASPADA", "TERKAIT"], "rows": [
    ["Suplai beredar (CMC)", "883,3 juta", "≤915 juta (22 Okt 2027)", "P1"],
    ["Unlock bulanan (tanggal 12)", "±1,75 juta APT (Messari)", "waspada &gt;4,5 juta", "P1"],
    ["APT dibakar 30 hari (on-chain)", "174.210", "≥500 ribu (30 Sep 2027)", "P2"],
    ["Transaksi harian (on-chain)", "9,7 juta", "≥28 juta", "P2"],
    ["Volume perpetual 7 hari", "$396,6 juta", "≥$1 miliar", "P2"],
    ["Stablecoin di Aptos (on-chain)", "$949 juta", "≥$1,5 miliar · waspada &lt;$700 juta", "P3 · R1"],
    ["TVL DeFi Aptos", "$43,2 juta", "waspada &lt;$30 juta", "R1"],
    ["Proposal imbalan staking / batas suplai", "2,6% · 2,1 miliar", "waspada usulan kenaikan", "R2"],
    ["Gangguan jaringan / peretasan", "tidak ada (Okt 2026)", "waspada halt ≥2 jam / ≥$10 juta", "R3"],
    ["APT tutup mingguan / BTC", "$0,822 / $82.941", "waspada &lt;$0,73 / &lt;$78.000", "Skenario"]
  ], "align": ["l", "r", "l", "r"]},
  {"type": "card", "label": "CARA MEMAKAI DASBOR INI", "mt": 10, "blocks": [
    {"type": "ul", "items": [
      f"{W('Dua indikator utama')} adalah suplai beredar (P1) dan APT yang dibakar (P2). Bila keduanya sesuai jalur, tesis berjalan.",
      f"{W('Tanda bahaya pertama')} adalah stablecoin di bawah $700 juta atau TVL di bawah $30 juta (R1); skenario Pesimis menjadi lebih mungkin.",
      f"{W('Status syariah')} perlu dicek ulang bila porsi fee dari Decibel dan dana tokenisasi berbunga naik (Lapis 3).",
      "Peluang menyentuh suatu harga tidak dihitung dalam skenario; level $0,73 dipakai sebagai batas waspada perjalanan harga."
    ]}
  ]},
  {"type": "card", "label": "SKOR FUNDAMENTAL 7,0 · KUAT (EST.)", "mt": 10, "blocks": [
    {"type": "bars", "label_width": 230, "max": 10, "rows": [
      {"label": "Tokenomics (bobot 30%)", "value": 7.55, "color": "green", "display": "7,6"},
      {"label": "Jaringan &amp; bisnis (30%)", "value": 6.1, "color": "gold", "display": "6,1"},
      {"label": "Nilai ke holder (25%)", "value": 6.75, "color": "gold", "display": "6,8"},
      {"label": "Risiko (15%, makin tinggi makin aman)", "value": 8.11, "color": "green", "display": "8,1"}]},
    {"type": "note", "html": "Kuat: unlock tinggal ±2,4% suplai beredar, seluruh fee dibakar. Lemah: pangsa pasar L1 kecil, TVL menyusut, hasil bersih holder negatif, 98% transaksi dari satu aplikasi. Aktivitas pengembang dan sebaran kepemilikan tidak dinilai (data tidak tersedia). Tanda bahaya: 1 dari 9 (jatah tim + investor 32,5%)."}
  ]},
  {"type": "card", "label": "TANDA BAHAYA (1 DARI 9 AKTIF)", "mt": 10, "blocks": [
    {"type": "table", "size": 9.5, "pad": 3, "cols": "repeat(3, minmax(0px,1fr))", "header": ["", "", ""], "rows": [
      [D("green", "Tim anonim: tidak"), D("green", "Tanpa audit: tidak"), D("orange", "Tim/VC &gt;30%: ya (32,5%)")],
      [D("green", "FDV/MC &gt;5×: tidak (1,37×)"), D("green", "Umur &lt;6 bulan: tidak"), D("green", "Tiruan: tidak")],
      [D("green", "Tanpa kegunaan: tidak"), D("green", "Janji imbal hasil: tidak"), D("green", "Pendiri jual besar: tidak terlihat")]
    ]},
    {"type": "note", "html": "Batas skor baru berlaku bila ≥3 tanda aktif."}
  ]},
  {"type": "card", "label": "RIWAYAT HARGA SINGKAT", "mt": 10, "blocks": [
    {"type": "bars", "label_width": 180, "max": 20, "rows": [
      {"label": "Puncak (30 Jan 2023)", "value": 19.9, "color": "muted", "display": "$19,90"},
      {"label": "20 Okt 2025", "value": 3.58, "color": "orange", "display": "$3,58"},
      {"label": "Terendah (30 Agu 2026)", "value": 0.513, "color": "red", "display": "$0,513"},
      {"label": "Kini (22 Okt 2026)", "value": 0.822, "color": "green", "display": "$0,822"}]},
    {"type": "note", "html": "CoinMarketCap dan Yahoo Finance (penutupan mingguan). Harga kini +60% dari titik terendah, tetapi masih −77% dalam 52 minggu."}
  ]}
]})

# ---------------- HAL 14: Sumber & glosarium ----------------
pages.append({"label": "Sumber dan glosarium", "subtitle": "Sumber &amp; glosarium", "disclaimer": "B", "blocks": [
  {"type": "bigsec", "num": "8", "title": "Sumber", "mt": 14},
  {"type": "text", "html": "Harga, MC, suplai: CoinGecko (±08.30 WIB 22 Okt 2026), dicek silang dengan CoinMarketCap. Beta: regresi return mingguan 52 minggu APT terhadap BTC dari Yahoo Finance (hitungan sendiri). Fee, TVL, stablecoin, RWA, volume: DefiLlama (21 Okt). Pembakaran dan APT baru: dasbor suplai resmi Aptos (21 Okt). Unlock dan staking: Messari/Blockworks Research (Okt 2026), dicek silang dengan Everstake (30 Sep). Skenario BTC: Pandangan Pasar Bulanan Shariacrypto Oktober 2026. Laporan Messari dibaca dari salinan pemilik; laporan itu dibiayai Aptos Foundation. " + logo_note + ".", "size": 10, "mt": 4},
  {"type": "resources", "items": [["CoinGecko APT", "coingecko.com"], ["CoinMarketCap APT", "coinmarketcap.com"], ["DefiLlama · Aptos", "defillama.com"], ["Dasbor suplai APT", "aptosnetwork.com"], ["Messari · Path to Deflation", "messari.io"], ["Pembaruan tokenomics", "aptosnetwork.com"], ["Jadwal unlock", "everstake.com"], ["Suplai bersih 1,5%", "tokenpost.com"], ["Pembakaran 174 ribu", "cryptobriefing.com"], ["Derivatif 21 Okt", "blockchain.news"], ["Riwayat harga", "finance.yahoo.com"], ["HalalScreener APT", "halalscreener.app"], ["Gangguan Okt 2023", "theblock.co"]]},
  {"type": "bigsec", "num": "9", "title": "Glosarium", "mt": 14},
  {"type": "text", "html": "Arti singkat istilah yang dipakai di dokumen ini, diurutkan sesuai kemunculannya.", "muted": True, "mb": 6},
  {"type": "grid", "mt": 0, "align": "start", "cols": "minmax(0px,1fr) minmax(0px,1fr)", "gap": 10, "items": [
    {"type": "table", "size": 9.5, "pad": 4, "cols": "112px minmax(0px,1fr)", "header": ["ISTILAH", "ARTI SINGKAT"], "rows": [
      [T("Gas · fee"), "Biaya transaksi di jaringan, dibayar dengan APT."],
      [T("Staking · staker · validator"), "Mengunci APT untuk menjaga jaringan; pelakunya mendapat imbalan APT baru."],
      [T("Burn (dibakar)"), "APT dimusnahkan sehingga suplai berkurang."],
      [T("Deflasi / inflasi bersih"), "Suplai menyusut / bertambah setelah dikurangi yang dibakar."],
      [T("Unlock"), "Token yang dikunci lalu dilepas ke pasar sesuai jadwal."],
      [T("TVL"), "Total aset yang disetor ke aplikasi DeFi di jaringan."],
      [T("Batas suplai (hard cap)"), "Jumlah maksimum APT yang boleh ada; kini 2,1 miliar."],
      [T("Stablecoin"), "Token yang nilainya dipatok ke dolar (USDT, USDC)."],
      [T("Market cap (MC) / FDV"), "Harga × suplai beredar / harga × seluruh suplai yang sudah ada."],
      [T("Beta"), "Seberapa besar APT bergerak saat BTC bergerak 1%; beta 1,32 berarti ±1,32%."],
      [T("L1 smart contract"), "Jaringan utama yang menjalankan aplikasi (Ethereum, Solana, Aptos)."],
      [T("Pendapatan holder"), "Bagian fee yang sampai ke holder lewat pembakaran, buyback, atau bagi fee (holders revenue)."],
      [T("Lama balik modal"), "Market cap ÷ pendapatan holder per tahun, dalam tahun."],
      [T("Perpetual · open interest · funding"), "Kontrak berjangka tanpa jatuh tempo / total posisi terbuka / biaya antar-posisi tiap 8 jam."],
      [T("RWA / tokenisasi"), "Aset dunia nyata (dana, obligasi) yang dibuatkan versi token."],
      [T("DEX · DeFi"), "Bursa tanpa perantara / layanan keuangan berbasis smart contract."]
    ]},
    {"type": "table", "size": 9.5, "pad": 4, "cols": "112px minmax(0px,1fr)", "header": ["ISTILAH", "ARTI SINGKAT"], "rows": [
      [T("Order book"), "Daftar pesanan beli dan jual; di Decibel setiap pesanan adalah transaksi."],
      [T("Sankey"), "Diagram aliran uang dari sumber ke tujuan."],
      [T("Tata kelola · AIP"), "Pemungutan suara holder yang di-stake / usulan perubahan Aptos."],
      [T("Mempool terenkripsi"), "Antrean transaksi yang isinya disembunyikan sampai masuk blok."],
      [T("Skenario Optimis · Dasar · Pesimis"), "Tiga kemungkinan harga akhir 12 bulan, dengan peluang dari Pandangan Pasar Bulanan."],
      [T("Alfa"), "Tambahan atau potongan poin persentase di target, karena pendorong/risiko khusus APT."],
      [T("Harga Perkiraan"), "Target tiap skenario dikali peluangnya, lalu dijumlah."],
      [T("Rasio Untung-Rugi (risk/reward, R/R)"), "Potensi naik ÷ potensi turun. ≥2 Harga Murah; 1–1,99 Harga Wajar; &lt;1 Harga Mahal."],
      [T("Fundamental"), "Skor 1–10 dari tokenomics, jaringan &amp; bisnis, nilai ke holder, dan risiko."],
      [T("Riba · maysir"), "Bunga · judi/untung-untungan."],
      [T("Tathir"), "Menyucikan harta dengan menyedekahkan bagian yang tidak halal."],
      [T("Halal Bersyarat"), "Lolos semua batas minimum dengan skor 60–79; boleh dengan syarat per aktivitas."],
      [T("Sikap"), "Saran tindakan dari gabungan label Fundamental dan Harga: Beli Bertahap sampai Hindari."],
      [T("Short covering"), "Penutupan posisi jual (short) yang ikut mendorong harga naik."],
      [T("Deposit penyimpanan"), "APT jaminan untuk data baru di jaringan; kembali bila data dihapus."],
      [T("Nakamoto coefficient"), "Jumlah validator minimum yang bila bersekongkol bisa menghentikan jaringan."]
    ]}
  ]},
  {"type": "note", "html": "Satuan: dolar AS; ribu, juta, miliar, triliun ditulis dengan kata. “(est.)” = perkiraan analis. “N/A” = data tidak tersedia untuk publik."}
]})

content = {
  "meta": {"title": "Shariacrypto Research Note — Aptos (APT) — 22 Okt 2026", "header_line": "Aptos (APT) · data 21–22 Okt 2026 · Metodologi v3.1"},
  "disclaimers": {
    "A": "Shariacrypto Research Note adalah produk riset internal. Bukan fatwa dan bukan saran investasi. Status syariah memakai kerangka 4 lapis Shariacrypto dan perlu ditinjau ulama yang kompeten. Data dari sumber publik (<span data-ed=\"1\">CoinGecko, CoinMarketCap, DefiLlama, dasbor suplai Aptos, Everstake</span>). Angka bertanda (est.) adalah perkiraan analis.",
    "B": "Dokumen ini untuk edukasi dan riset internal Shariacrypto. BUKAN saran investasi. BUKAN fatwa. Status syariah adalah hasil analisis mandiri; konsultasikan dengan Dewan Syariah yang kompeten sebelum mengambil keputusan.",
    "EXEC": "Edukasi dan riset internal Shariacrypto; BUKAN saran investasi, bukan fatwa. Halal Bersyarat tidak sama dengan investasi bagus. Pengungkapan: per tanggal data, aset ini tidak termasuk daftar kepemilikan Grup Eksklusif Shariacrypto. Harga per <span data-ed=\"1\">±08.30 WIB 22 Okt 2026</span>; fee &amp; TVL per 21 Okt. Glosarium hal. 16."
  },
  "pages": pages
}
json.dump(content, open('content_APT.json', 'w'), ensure_ascii=False, indent=1)
print('pages', len(pages))
