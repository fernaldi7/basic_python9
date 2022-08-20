# mylist = ["Pisang", "Apel", "Ceri"]

# mytuple = ("Semangka", "Nanas", "Jeruk")

# list1 = list(mytuple)
# list1[0] = "Manggis"
# mytuple = tuple(list1)
# print(mytuple)

mylist = ["Pisang", "Apel", "Ceri"]
myset = {"Semangka", "Semangka", "Nanas", "Jeruk", "Jeruk", "Banana"}
myset.remove("Banana")
for x in myset:
    print(x)