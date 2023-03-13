import sys

a = b = 4000
print(id(a))
print(id(b))

b = 3000
print(id(a))
print(id(b))
print(a)

a = 30.6
b = "tekst"
c = True
print(type(c))

l1 = 2345
l2 = 2345
print(id(l1))
print(id(l2))
print(bool(1))
int(100)

print(5**2)
print(5//3)


#kalkulator powinien zawierac
print("Tak" == "tak")
ord("T")
ord("t")
chr(66)
chr(12)
a = "zmienna a"
b = "zmienna b"
f"{a} to jest lancuch wartosc b {b}"
print(f"{a} to jest lancuch wartosc b {b}")

print(a.lower())
print(b.lower())
print(b.title())

a = 20

if a > 21 :
    print("a wieksze od 21")
elif a < 21 :
    print("a")
else :
    print("k")


print(sys.getrefcount(a))
print (sys.version)


