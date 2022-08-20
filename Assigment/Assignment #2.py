nama = ['']
tel = ['']

def daftar():
    print("Daftar Kontak : \i")
    for i in range (len[nama]):
        print ("Nama : " + nama[i])
        print ("Nomor Telepon : " + tel[i])
        print("")

def tambah():
    while True:
        try:
            nama.append(str(input("Nama : ")))
            break
        except ValueError:
            print("Input Nama belum sesuai")

    while True:
        try:
            tel.append(int(input("Nomor Telepon: ")))
            break
        except ValueError:
            print("Input Nomor Telepon Belum Sesuai")
    print("Kontak Berhasil Ditambahkan")
    print("")
    
print('Selamat Datang !')
while True:
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    while True:
        try:
            menu = int(input("Pilih menu: "))
            break
        except ValueError:
            print("Pilih sesuai menu")

    if menu == 1:
        daftar()
    elif menu == 2:
        tambah()
    elif menu == 3:
        print(" Program Selesai. Sampai Jumpa !")
        break
    else :
        print("Menu Tidak Tersedia\n")