revenue = int(input("Выручка: "))
costs = int(input("Издержки: "))
if revenue > costs:
    profit = revenue - costs
    print(f"Прибыль составляет: {profit}")
    print(f"Ретабельность составяет: {profit / revenue * 100:.3f}")
    staff = int(input("Численность сотруднков: "))
    print(f"Прибыль на одного сотрудника ранва: {profit / staff}")
elif revenue == costs:
    print("Прибыль равна: 0 \nУбыток равен: 0")
else:
    print(f"Убыток равен: {revenue - costs}")