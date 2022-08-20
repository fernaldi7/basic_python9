#Soal2
Π = 22/7
while True:
    try:
        r = float(input("Jari-jari: "))
        break
    except ValueError:
        print ("Input jari-jari belum sesuai")
Luas_lingkaran = Π*r*r
perhitungan = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r, Luas_lingkaran)

print(perhitungan)