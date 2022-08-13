def salam():
    print("Selamat pagi")

def halo():
    print("halo, selamat pagi")

#call a function
salam()
halo()

'''
def perkenalan(nama, umur, domisili):
    salam()
    print(f"Halo, nama saya {nama}, umur {umur}, domisili {domisili}")

perkenalan("Aldi", 22, "Semarang")
'''

def perkenalan(nama, umur=32, domisili="Amstredam"):
    salam()
    print(f"Halo, nama saya {nama}, umur {umur}, domisili {domisili}")

perkenalan("Aldi", 22, "Semarang")

def perkalian(a, b):
    total = a * b
    print(f"{a} x {b} = {total}")
    return total

perkalian(4, 2)