#ögrenci: Halis Ensar Yıldız
#Numara: 20253004032
#Github deposu:https://github.com/xelhys/uzay-oyunu
import json
from pathlib import Path
def envanter_metni(credits: bool, engines: bool , copilot: bool) -> str:
    bilesenler =[]
    if credits:
        bilesenler.append("bol kredi")
    if engines:
        bilesenler.append("guclu motorlar")
    if copilot:
        bilesenler.append("yetenekli bir pilot")

    if not bilesenler:
        return ""

    return f"Sende: {', '.join(bilesenler)}"

def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)

dosya_yolu = Path(__file__).with_name("galaksi.json")

with dosya_yolu.open(encoding="utf-8") as dosya:
    galaksi = json.load(dosya)

print(galaksi)
    