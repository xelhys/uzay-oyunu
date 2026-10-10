import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_bazi_bilesenler():
    assert envanter_metni(True, False, True) == "Sende: bol kredi , yetenekli bir pilot"


def test_hedef_menusu():
    hedefler = ["centauri","sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centuari\n[2] sirius"
    assert hedef_menusu(["centauri" "sirius"]) == beklenen
