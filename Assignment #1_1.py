#Soal1
import sys
while True:
    try:
        Nama = str(input("Nama: "))
        break
    except ValueError:
        print ("Input nama belum sesuai")
while True:
    try:
        Umur = int(input("Umur: "))
        break
    except ValueError:
        print ("Input umur belum sesuai")
while True:
    try:
        Tinggi = float(input("Tinggi: "))
        break
    except ValueError:
        print ("Input tinggi belum sesuai")

biodata = "Nama saya {}, umur saya {} tahun dan tinggi saya {} cm.".format(Nama,Umur,Tinggi )

print(biodata)