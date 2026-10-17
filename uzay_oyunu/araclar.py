#ögrenci: Halis Ensar Yıldız
#Numara: 20253004032
#Github deposu:https://github.com/xelhys/uzay-oyunu
def hamle_sayaci():
    sayac = 0

    def say():
        nonlocal sayac
        sayac +=1
        return sayac

    return say

def en_bagli_gezegenler(galaksi):

    return sorted(
        galaksi["baglantilar"].keys(),
        key=lambda gezegen: (-len(galaksi["baglantilar"][gezegen]), gezegen),
    )

#Bonus  
import time
def sure_olc(fonksiyon):
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        gecen_sure = bitis - baslangic
        print(f"{fonksiyon.__name__} calisma suresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici