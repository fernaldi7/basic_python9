''''
nama = "Andi"
umur = 35

biodata = "nama saya adalah {}, saya berumur {} tahun".format(nama, umur)
biodata_2 = f"nama saya adalah {nama}, saya berumur {umur} tahun"

print(biodata)
print(biodata_2)
'''
'''
x = 9
y = 10
z = 10

print(x > y)
print(x < y)
print(z == y)
'''

'''
x = 100
y = 200

if x > y:
    print("x lebih besar dari y")
else:
    print("x lebih kecil dari y")
'''
'''
myList = [1, 2, 3, 4, 5]
print(myList)
print(type(myList))

myList2 = [1, "Indonesia", 2.09]
print(myList2)
print(type(myList2))
myList2.append(2)
'''
'''
a = 200
b = 30
if a < b:
    print("a lebih kecil dari b")
elif a ==b:
    print("a sama dengan b")
elif a <=b:
    print("a kurang dari sama dengan b")
else:
    print("a lebih besar dari b")
'''

a = 300
b = 200
c = 200

if b == c and b > a:
    print("ini adalah benar")
else:
    print("ini adalah salah") 