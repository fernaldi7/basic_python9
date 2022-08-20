
# class program

class mentee():
    nama = "Default"
    umur = "Default"
    nim = "Default"

    def __init__(self, input_nama, umur, nim):
        self.nama = input_nama
        self.umur = input_umur
        self.nim = input_nim

    # def belajar(self):
    #     print(self.nama, "sedang belajar")

    # def istirahat(self, kondisi):
    #     print(self.nama, "sedang istirahat di kantin", kondisi)

# main program
sari = mentee("Sari Masari", 27, "21010117130114")
jeje = mentee("Jeje Majeje", 25, "21017854643278")

print(sari)
# sari.nama = "Sari Masari"
# jeje.nama = "Jeje Majeje"

# sari.umur = 27
# jeje.umur = 23

# print(sari.nama) 
# print(jeje.nama)

# print(sari.umur)
# print(jeje.umur)

# sari.belajar()
# jeje.istirahat("bersama-sama dengan temannya")