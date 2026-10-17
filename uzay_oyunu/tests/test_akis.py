#ögrenci: Halis Ensar Yıldız
#Numara: 20253004032
#Github deposu:https://github.com/xelhys/uzay-oyunu
from itertools import islice
import pytest

from uzay_oyunu.akis import (
    fibonacci,
    yakit_gostergesi,
    satirlari_oku,
    ayristir,
    uzun_yolculuklar,
    rota_sayaci,
)

def test_fibonacci_ilk_degerler() -> None:

    g = fibonacci
    assert(next(g),next(g),next(g)) == (0,1,1)

    beklenen_12 = [0,1,1,2,3,5,8,13,21,34,55,89]
    assert list(islice(fibonacci(),12)) == beklenen_12

def test_fibonacci_tek_kullanimlik() -> None:
    g = fibonacci()
    ilk_5 = list(islice(g,5))
    ikinci_5 = list(islice(g,5))

    assert ilk_5 == [0,1,1,2,3]
    assert ikinci_5 == [5,8,13,21,34]
    assert ilk_5 != ikinci_5

def test_yakit_gostergesi_degerler() -> None:
    assert list(yakit_gostergesi(100,30)) == [70,40,10,0]

def test_yakit_gostergesi_stopiteration() -> None:

    g = yakit_gostergesi(20,10)
    assert next(g) == 10
    assert next(g) == 0

    with pytest.raises(StopIteration):
        next(g)

def test_boru_hatti_ayristir_ve_suz() -> None:
    
    ornek_satirlar = [
        "dünya -> sirius 12",
        "sisius -> orion 8",
        "orion -> centauri 15",
    ]
kayitlar = list(ayristir(ornek_satirlar))
assert kayitlar == [
    ("Dunya", "sirius",12),
    ("sirius", "orion", 8),
    ("orion", "centauri", 15),
    ]

uzunlar = list(uzun_yolculuklar(kayitlar, 10))
hedefler = [h for _, h, _ in uzunlar]
assert hedefler == ["sirius", "centauri"]

def test_rota_sayaci() -> None:
    baglantilar = {
        "Dunya": ["Mars"],
        "Mars" : ["Venus"],
        "Venus" : ["Dunya"],
    }
say = rota_sayaci(baglantilar)

assert say("Dunya", 0) == 1
assert say("Dunya", 3) == 1
assert say("Dunya", 10) == 1
assert say("Dunya", 40) == 1