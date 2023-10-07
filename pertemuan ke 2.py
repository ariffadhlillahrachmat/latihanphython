class mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

saya = mahasiswa("tatang","221024")
print("nama saya adalah", saya.nama)
print("nim saya adalah",saya.nim)

class mahasiswa:
    def __init__(self,nama,nim,umur):
     self.nama = nama
     self.nim = nim
     self.umur = umur 

    def __str__(self):
     return f"nama saya adalah {self.nama}, {self.nim} dan nim saya adalah {self.nim}"
    
    def tahunlahir(self):
      return 2023 - self.umur
    

class mahasiswa:
   def __init__(self,nama,nim,umur):
      self.nama = nama 
      self.nim = nim
      self.nama = umur

   def __str__(self):
     return f"nama saya adalah{self.nama},dan nim saya adalah {self.nim}"
   
   def tahunlahir(self):
    return 2023 - self.umur
   
   saya = mahasiswa("ujang","089285",21)
   print("tahun lahir saya adalah",saya.tahunlahir())
   print("saya tatang angkatan","089285" [0:14])