import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family':'Inter','font.size':10})
BG='#072E1A'; GRID='#1E4A2A'; TXT='#E8F0EA'; MUT='#8FA89A'; G='#16C784'; Y='#FFC107'; R='#FF8A8A'; B='#40C4FF'; O='#EF9F27'
def idr(x,d=1): return f"{x:,.{d}f}".replace(',','X').replace('.',',').replace('X','.').replace('-','−')
def setup(h=4.6,w=10):
    fig=plt.figure(figsize=(w,h),dpi=150); fig.patch.set_facecolor(BG)
    ax=fig.add_axes([0.095,0.15,0.865,0.60]); ax.set_facecolor(BG)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(colors=MUT,length=0); ax.grid(axis='y',color=GRID,lw=.8); ax.set_axisbelow(True)
    return fig,ax
def frame(fig,title,sub,src):
    fig.text(0.035,0.965,title,color=TXT,fontsize=14.5,fontweight='bold',va='top')
    fig.text(0.035,0.875,sub,color=MUT,fontsize=8.8,va='top')
    fig.text(0.965,0.02,src,color=MUT,fontsize=7.3,ha='right')
# 1 proyeksi suplai
fig,ax=setup(h=3.6)
yrs=np.arange(2026,2101)
sc=[('Aturan lama (+60 jt/th)',60,MUT,(0,(5,3))),('Staking naik (+29 jt/th)',29,O,'-'),('Laju kini (+16 jt/th)',16,Y,'-'),('P2 tercapai (+12 jt/th)',12,B,'-'),('Dibakar ≥ APT baru',0,G,'-')]
ax.axhline(2100,color=R,lw=1.4); ax.text(2027,2135,'Batas 2,1 miliar APT',color=R,fontsize=9,fontweight='bold')
for lab,n,c,ls in sc:
    y=np.minimum(1209+n*(yrs-2026),2100); ax.plot(yrs,y,color=c,lw=2.2,ls=ls)
    hit=2026+891/n if n else None
    ytxt=y[-1] if not hit or hit>2100 else 2100
    if hit and hit<=2100: ax.plot([hit],[2100],'o',ms=6,color=c); ax.text(hit,2050,f'±{int(round(hit))}',color=c,fontsize=8.5,ha='center',va='top')
    ax.text(2101,y[-1] if n==0 or (hit and hit>2100) else 2100,'',color=c)
ax.text(2101,1209,'Dibakar ≥\nAPT baru',color=G,fontsize=8.5,va='center')
ax.text(2034,1209+60*8,'Aturan lama',color=MUT,fontsize=8.5,ha='right')
ax.text(2047,1209+29*21-20,'Staking naik',color=O,fontsize=8.5,va='top')
ax.text(2068,1209+16*42-20,'Laju kini',color=Y,fontsize=8.5,va='top')
ax.text(2088,1209+12*62-25,'P2 tercapai (±2100)',color=B,fontsize=8.5,va='top')
ax.set_xlim(2026,2112); ax.set_ylim(1100,2250)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v,p: idr(v/1000,1)+' M'))
frame(fig,'Batas 2,1 miliar baru “menggigit” ±56 tahun lagi pada laju kini','Suplai total APT (miliar) bila suplai bersih per tahun tetap; dihitung dari ruang ±891 juta di bawah batas','Data s.d. 22 Okt 2026 · Sumber: dasbor suplai Aptos, Blockworks Research; hitungan Shariacrypto (est.)')
fig.savefig('c_proyeksi.png',facecolor=BG); plt.close(fig)
# 2 unlock per 12 bulan
fig,ax=setup(h=3.4)
per=['Okt23–\nSep24','Okt24–\nSep25','Okt25–\nSep26','Okt26–\nSep27','Okt27–\nSep28','Okt28–\nSep29','Okt29–\nSep30','Okt30–\nSep31','Okt31–\nSep32']
val=[135.7,135.7,135.7,20,20,20,20,20,20]
cols=[O,O,O,G,G,G,G,G,G]
ax.bar(range(9),val,color=cols,width=.62)
for i,v in enumerate(val): ax.text(i,v+3,('±' if i>2 else '')+idr(v,0 if i>2 else 1),color=TXT,ha='center',fontsize=9,fontweight='bold')
ax.axhline(19.4,color=Y,lw=1.4,ls='--'); ax.text(8.45,75,'Garis kuning: APT baru dari staking\n±19,4 jt/th, terpisah dari unlock',color=Y,fontsize=8.5,ha='right',va='bottom')
ax.axvline(2.5,color=MUT,lw=1,ls=':'); ax.text(2.55,128,'12 Okt 2026:\ntim & investor selesai',color=MUT,fontsize=8,va='top')
ax.set_xticks(range(9)); ax.set_xticklabels(per,fontsize=8.5,color=MUT); ax.set_ylim(0,155)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v,p: idr(v,0)))
frame(fig,'Token yang dilepas ke pasar turun ±85% mulai Oktober 2026','Unlock per 12 bulan (juta APT): tim, investor, komunitas, dan yayasan; tidak termasuk APT baru dari staking','Sumber: Everstake (11,31 jt/bln s.d. Sep 2026), Blockworks Research (±119 jt s.d. 2032); hitungan Shariacrypto (est.)')
fig.savefig('c_unlock.png',facecolor=BG); plt.close(fig)
# 3 sumber fee
fig,ax=setup(h=3.4); ax.grid(axis='x',color=GRID,lw=.8); ax.grid(axis='y',visible=False)
items=[('Securitize · dana tokenisasi (mayoritas berbasis bunga)',623,O),('Decibel · perpetual berleverage',559,R),('Jaringan Aptos · gas dibakar',141,G),('Echelon · pinjaman berbunga',64,R),('DEX spot · Thala, Hyperion, PancakeSwap',32,G)]
for i,(l,v,c) in enumerate(items[::-1]):
    ax.barh(i,v,color=c,height=.42); ax.text(v+8,i,f'${v} ribu',color=TXT,va='center',fontsize=9,fontweight='bold'); ax.text(4,i+.26,l,color=MUT,fontsize=8.5,va='bottom')
ax.set_yticks([]); ax.set_xlim(0,760); ax.set_ylim(-.5,4.9)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v,p: f'${int(v)} rb'))
frame(fig,'±97% fee aplikasi di Aptos datang dari dana berbunga, perpetual, dan pinjaman','Fee 30 hari per aplikasi (dolar AS). Merah/oranye: aktivitas yang dinilai riba atau maysir; hijau: gas jaringan dan pertukaran spot','Data 21 Okt 2026 · Sumber: DefiLlama; klasifikasi Shariacrypto')
fig.savefig('c_fee.png',facecolor=BG); plt.close(fig)
# 4 valuasi scatter
fig,ax=setup(h=3.45); ax.set_position([0.095,0.21,0.865,0.55]); ax.grid(axis='both',color=GRID,lw=.6)
pts=[('Aptos (laju kini)',1.72e6,726.5e6,G),('Aptos (12 bln)',0.87e6,726.5e6,G),('Ethereum',40.5e6,306.6e9,B),('Solana',42.7e6,63.5e9,Y),('NEAR',1.06e6,7.0e9,O),('Sui',9e3,4.3e9,R)]
x=np.logspace(3,8.5,50)
for m,l in [(100,'100 th'),(1000,'1.000 th'),(10000,'10.000 th'),(100000,'100.000 th')]:
    ax.plot(x,x*m,color=MUT,lw=.8,ls=':'); 
for m,l,xx in [(100,'balik modal 100 th',1.2e8),(1000,'1.000 th',6e6),(10000,'10.000 th',2.0e7),(100000,'100.000 th',2.0e6)]:
    ax.text(xx,xx*m*0.55,l,color=MUT,fontsize=7.5,rotation=24,ha='right')
for l,xv,yv,c in pts:
    ax.plot([xv],[yv],'o',ms=9 if 'Aptos' in l else 7,color=c,mec=BG)
    off=(1.3,1.0) if l!='Aptos (12 bln)' else (0.75,1.0)
    ax.text(xv*off[0],yv*off[1],l,color=c,fontsize=8.8,fontweight='bold',ha='left' if l!='Aptos (12 bln)' else 'right',va='center')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(2e3,3e8); ax.set_ylim(2e8,1e12)
def usd(v,p):
    if v>=1e12: return '$'+idr(v/1e12,0)+' T'
    if v>=1e9: return '$'+idr(v/1e9,0)+' M'
    if v>=1e6: return '$'+idr(v/1e6,0)+' jt'
    return '$'+idr(v/1e3,0)+' rb'
ax.xaxis.set_major_formatter(FuncFormatter(usd)); ax.yaxis.set_major_formatter(FuncFormatter(usd))
ax.set_xlabel('Pendapatan holder per tahun (fee dibakar/dibagikan, skala log)',color=MUT,fontsize=9); ax.set_ylabel('Market cap (skala log)',color=MUT,fontsize=9)
frame(fig,'Dari sisi pendapatan holder, APT termurah di antara L1 pembanding','Market cap ÷ pendapatan holder per tahun = lama balik modal; makin ke kanan-bawah, makin murah. “M” = miliar','Data 21–22 Okt 2026 · Sumber: DefiLlama (24 jam × 365), CoinGecko; hitungan Shariacrypto (est.)')
fig.savefig('c_valuasi.png',facecolor=BG); plt.close(fig)
# 5 kipas skenario
fig,ax=setup(h=3.5)
P=0.8222; sc=[('Optimis',1.531,.20,G),('Dasar',1.095,.55,B),('Pesimis',0.445,.25,R)]
for n,t,p,c in sc:
    ax.plot([0,12],[P,t],color=c,lw=2+6*p,alpha=.85,solid_capstyle='round')
    ax.text(12.25,t,f'{n} ${idr(t,3)}  ({"+" if t>P else ""}{idr((t/P-1)*100,0)}%) · peluang {int(p*100)}%',color=c,fontsize=9,va='center',fontweight='bold')
ax.plot([0,12],[P,1.019],color=TXT,lw=1.4,ls='--'); ax.text(12.25,1.019+0.0,'',color=TXT)
ax.text(6,0.97,'Harga Perkiraan $1,019 (+24%)',color=TXT,fontsize=8.5,rotation=6)
ax.plot([0],[P],'o',ms=9,color=TXT); ax.text(-0.3,P,'Kini\n$0,822',color=TXT,fontsize=9,ha='right',va='center')
ax.axhspan(0.73,0.78,color=Y,alpha=.12); ax.text(0.4,0.70,'Zona beli $0,73–0,78',color=Y,fontsize=8.5,va='top')
ax.set_xlim(-2,22); ax.set_ylim(0.3,1.7); ax.set_xticks([0,3,6,9,12]); ax.set_xticklabels(['Okt 26','Jan 27','Apr 27','Jul 27','Okt 27'],color=MUT)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v,p:'$'+idr(v,2)))
frame(fig,'Rasio Untung-Rugi 3,1×: potensi naik tiga kali potensi turun','Harga akhir 12 bulan per skenario; tebal garis = peluang. Bukan jalur harga, hanya titik awal dan titik akhir','Peluang: Pandangan Pasar Shariacrypto Okt 2026 · beta 1,32 · hitungan Shariacrypto')
fig.savefig('c_kipas.png',facecolor=BG); plt.close(fig)
