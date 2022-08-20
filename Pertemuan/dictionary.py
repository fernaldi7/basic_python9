# how to create a dictionary

mahasiswa1 = {
    "nama": "Frans",
    "nim": 1,
    "kelas": "B120",
    "status": "aktif"
}

mahasiswa2 = {
    "nama": "Sarah",
    "nim": 2,
    "kelas": "B121",
    "status": "pasif"
}

mobil1 = {
    "brand": "toyota",
    "model": "innova",
    "year": 2022,
}

mobil2 = {
    "brand": "honda",
    "model": "crv",
    "year": 2021,
}

print(mobil1)
print(mobil2)

# mengakses dictionary
print(mobil1["model"])

# mengubah value dictionary
mobil1["model"] = "fortuner"
print(mobil1["model"])

# menambahkan value dalam dictionary
mobil1["seri"] = "Q35455DD"
print(mobil1)