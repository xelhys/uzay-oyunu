def yakit_ekle(miktar, depo = None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_bagimsiz_depo():
    depo1 = yakit_ekle(10)
    assert depo1 == [10]

    depo2 = yakit_ekle(20)
    assert depo2 == [20]


'''python
x = 10 

def oku():
    print(x)

oku()
'''

x =10

def hata_ver():
    print(x)
    x = 20
    
hata_ver()