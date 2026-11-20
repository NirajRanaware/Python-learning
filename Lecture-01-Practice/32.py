a = 12
b = 5
c = 3

a = a // b + c ** 2
b = a % c + b
c = a + b * c

print(a)
print(b)
print(c)
print(a + b + c)