n = int(input("Число: "))
nn = n * 10 + n
nnn = n * 100 + n * 10 + n
print(n + nn + nnn)

# 2 способ с конкатенацией
a = str(n)
c = a + a
v = a + a + a
print(n + int(c) + int(v))