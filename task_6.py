a = int(input("Первый результат: "))
b = int(input("Окончательный результат: "))
counter = 1
while a <= b:
    counter += 1
    a = a + a * 10 / 100
print(f"На {counter} день спротсмен достиг результата - {a:.2f}")
