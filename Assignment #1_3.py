#Soal 3
while True:
    try:
        Nilai_Ujian_Praktek = float(input("Nilai Ujian Praktek: "))
        break
    except ValueError:
        print ("Input nilai ujian belum sesuai")

while True:
    try:
        Nilai_Ujian_Teori = float(input("Nilai Ujian Teori: "))
        break
    except ValueError:
        print ("Input nilai ujian belum sesuai")

if Nilai_Ujian_Praktek > 70 and Nilai_Ujian_Teori > 70:
    print("Selamat, anda lulus!")
elif Nilai_Ujian_Teori >= 70 and Nilai_Ujian_Praktek < 70:
    print("Anda harus mengulang ujian praktek.")
elif Nilai_Ujian_Praktek >= 70 and Nilai_Ujian_Teori < 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.") 
