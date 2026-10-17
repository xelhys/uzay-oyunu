#ögrenci: Halis Ensar Yıldız
#Numara: 20253004032
#Github deposu:https://github.com/xelhys/uzay-oyunu
from functools import partial, reduce
def buyuk_harfli_gezegenler_map(gezegenler: list[str]) -> list[str]:
    return list(map(str.upper, gezegenler))

def buyuk_harfli_gezegenler_comp(gezegenler: list[str]) -> list[str]:
    return [g.upper() for g in gezegenler]

def en_az_iki_baglanti_filter(baglantilar: dict[str, list[str]]) -> list[str]:
    return list(filter(lambda g: len(baglantilar[g]) >=2, baglantilar))

def en_az_iki_baglanti_comp(baglantilar: dict[str, list[str]]) -> list[str]:
    return [g for g, komsular in baglantilar.items() if len(komsular) >=2]

def toplam_baglanti_reduce(baglantilar: dict[str, list[str]]) -> int:
    return  reduce(lambda toplam, komsular: toplam+ len(komsular), baglantilar.values(), 0)

def toplam_baglanti_sum(baglantilar: dict[str, list[str]]) -> int:
    return sum(len(komsular) for komsular in baglantilar.values())

def yolculuk(kaynak: str, hedef:str, hiz: int = 1) -> str:
    return f"{kaynak} -> {hedef} yolculuğu hiz = {hiz}'la tamamlandi"

hizli_yolculuk = partial(yolculuk, hiz=3)

if __name__ == "__main__":
    galaksi = {
        "gezegenler": ["dünya","centauri","sirius","orion","kara_delik"],
        "baglantilar": {
            "dünya": ["sirius","orion"],
            "centauri": ["sirius","orion"],
            "sirius": ["dünya","centauri","kara_delik"],
            "orion": ["dünya","centauri","sirius"],
            "kara_delik": ["sirius"]
        }
    }

print(buyuk_harfli_gezegenler_map(galaksi["gezegenler"]))

print(en_az_iki_baglanti_filter(galaksi["baglantilar"]))

print(toplam_baglanti_reduce(galaksi["baglantilar"]))