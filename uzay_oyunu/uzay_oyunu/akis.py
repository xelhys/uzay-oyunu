#ögrenci: Halis Ensar Yıldız
#Numara: 20253004032
#Github deposu:https://github.com/xelhys/uzay-oyunu
def fibonacci():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a+b
g = fibonacci()
print(next(g))
print(next(g))
print(next(g))

from itertools import islice, takewhile
print(list(islice(fibonacci(),12)))
print(list(takewhile(lambda x:x<100, fibonacci())))

def yakit_gostergesi(yakit: int,tuketim: int):
    while yakit>0:
        yakit = max(yakit-tuketim,0)
        yield yakit
    if yakit ==0:
        return

print(list(yakit_gostergesi(100,30)))

g = yakit_gostergesi(100,30)
print(next(g),next(g),next(g),next(g))
try:
    next(g)
except StopIteration:
    print("Yakit bitti!")

from pathlib import Path

def satirlari_oku(yol):
    with open(yol,encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()
            if satir and not satir.startswith("#"):
                yield satir

def ayristir(satirlar):
    for s in satirlar:
        rota,yakit = s.rsplit(" ",1)
        kaynak,hedef = rota.split("->")
        yield kaynak.strip(),hedef.strip(),int(yakit)

def uzun_yolculuklar(kayitlar, esik):
    for k in kayitlar:
        if k[2] > esik:
            yield k

dosya = Path("veri/seyir.txt")
if not dosya.exists():
    dosya = Path(__file__).resolve().parent.parent / "veri" / "seyir.txt"

print(sum(y for _, _, y in ayristir(satirlari_oku(dosya))))

kayitlar = ayristir(satirlari_oku(dosya))
print([h for _, h, _ in uzun_yolculuklar(kayitlar, 10)])

from functools import lru_cache 
import json
import time
def rota_sayaci(baglantilar):
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen,adim):
        if adim == 0:
            return 1
        return sum(rota_sayisi(h,adim-1)
                   for h in baglantilar.get(gezegen, [])
        )
        
        
    return rota_sayisi
    
json_yolu = Path(__file__).resolve().parent / "galaksi.json"
if not json_yolu.exists():
    json_yolu = Path("galaksi.json")

with open(json_yolu, "r", encoding="utf-8") as f:
    galaksi = json.load(f)   
    
    say= rota_sayaci(galaksi["baglantilar"])
    print(say("Dunya", 3))
    print(say("Dunya", 10))
    print(say("Dunya", 40))

def onbelleksiz_rota(gezegen,adim):
    if adim == 0:
        return 1
    return sum(
        onbelleksiz_rota(h,adim-1)
        for h in galaksi["baglantilar"].get(gezegen, [])
    )

t0 = time.perf_counter()
onbelleksiz_rota("Dunya", 20)
t_onbelleksiz = time.perf_counter() - t0

say.cache_clear()
t0 = time.perf_counter()
say("Dunya", 20)
t_onbellekli = time.perf_counter() - t0

print(f"\nÖnbelleksiz Süre: {t_onbelleksiz:.2f} saniye")
print(f"\nÖnbellekli Süre: {t_onbellekli:.2f} saniye")
print(f"\nCache Bilgisi: {say.cache_info()}")