# Ini Local Scope
# def myfunc():
#     x = 300
#     print(x)

# myfunc()

# Ini global scope
x = 300
def myfunc():
    x = 200
    print(x)

myfunc()
print(x)