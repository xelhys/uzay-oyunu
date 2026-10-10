#ögrenci: Halis Ensar Yıldız
#Numara: 20253004032
#Github deposu:https://github.com/xelhys/uzay-oyunu
def gorev_kaydi(baslik , *adimlar , oncelik= "normal", **ekler):
    print(f"[{oncelik.upper()}] {baslik}")
    for i, adim in enumerate(adimlar, start=1):
        print(f" {i}. {adim}")
    for anahtar, deger in ekler.items():
        print(f" {anahtar}: {deger}")



    if __name__ == "__main__":
        gorev_kaydi(
        
                "Kara delige atla",
                "Kredi kazan",
                "Pilot bul",
                "hiperdrive al",
                oncelik="yuksek",
                sorumlu="Ayse",
        )

        adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
        ek_bilgiler = {"Sorumlu":"Ayse"}


        gorev_kaydi(
            "Kara delige atla",
            *adim_listesi,
            oncelik = "yuksek",
            **ek_bilgiler,
        )