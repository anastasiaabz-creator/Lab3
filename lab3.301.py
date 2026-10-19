results = []

# Повторюємо двічі
for test in range(2):
    a = int(input("Введіть число: "))  # сума
    b = int(input("Введіть число: "))  # добуток

    # Перебираємо менше з чисел x від 1 до 1000
    for x in range(1, 1001):
        y = a - x

        if x <= y and x * y == b:
            results.append((x, y))
            break

for x, y in results:
    print(x, y)

