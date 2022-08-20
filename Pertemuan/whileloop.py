list_kota = ["jakarta", "bandung", "bogor", "tangerang", "bekasi"]

i = -1

while i < len(list_kota):
    i += 1
    if i % 2 == 0 and 1 > 0:
        print("skip")
        continue

    print(list_kota[1])