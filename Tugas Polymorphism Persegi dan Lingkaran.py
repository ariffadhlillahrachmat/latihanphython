class LuasPersegi:
    def hitung_luas(self):
        pass

class Persegi(LuasPersegi):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

def hitung_dan_cetak_luas(bentuk):
    print("Aku Adalah Persegi")
    print("Luas Persegi Dengan Sisi 4 Adalah :", bentuk.hitung_luas())

persegi = Persegi(4)
hitung_dan_cetak_luas(persegi)


class LuasLingkaran:
    def hitung_luas(self):
        pass

class Lingkaran(LuasLingkaran):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 3.14  * self.jari_jari ** 2

def hitung_dan_cetak_luas(bentuk):
    print("\nAku Adalah Lingkaran")
    print("Luas Lingkaran Dengan Jari-Jari 7 Adalah :", bentuk.hitung_luas())

lingkaran = Lingkaran(7)

hitung_dan_cetak_luas(lingkaran)
