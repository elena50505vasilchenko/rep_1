num = int(input("Число: "))
max_1 = 0
min_1 = 10
while num != 0:
    num_1 = num % 10
    if num_1 > max_1:
        max_1 = num_1
    if num_1 < min_1:
        min_1 = num_1
    num = num // 10
print(f"Максимальное число: {max_1} \nМинимальное число: {min_1}")