a = 8
b = 3
c = 2

x = a + b * c ** 2
y = x // b + a % c
z = (x + y) / (a - b)

a += int(z)
b *= int(x / y)
c = a % b

print(a)
print(b)
print(c)
print(x)
print(y)
print(z)