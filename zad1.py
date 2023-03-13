a = b = c = "Python 2023"
print(id(a) == id(b))
print(id(b) == id(c))

print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
c = "Java 11"
print (" ------------------------ ")
print(id(a) == id(b))
print(id(b) == id(c))

print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))