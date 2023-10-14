class Orang():
    def init(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname

class Alamat():
    def init(self, jalan, kota):
        self.jalan = jalan
        self.kota = kota
    def getjalan(self):
        return self.jalan
    def getkota(self):
        return self.kota



class Mahasiswa(Orang,Alamat):
    def __init__(self, firstname, lastname, nim, jalan, kota):
        self.nim=nim
        self.jalan=jalan
        self.kota=kota
        Orang.init(self, firstname, lastname)
        Alamat.init(self, jalan, kota)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} {self.nim} {self.jalan} {self.kota}"

    def printData(self):
        print(f"Nama  : {self.getfirstname()} {self.lastname}")
        print(f"NIM   : {self.nim}")
        print(f"Alamat: {self.jalan}, {self.kota}")

mhs = Mahasiswa("arif", "fadhlillah rachmat", "2207014", "tarogong kaler", "kota Garut")
mhs.printData()