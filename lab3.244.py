n = int(input("Введіть число: "))

if n <= 0:
    print("Число n має бути більшим за 0")
else:
    result = []
    # Перебираємо всі двоцифрові числа від 10 до 99
    for i in range(10, 100):
        first_digit = i // 10
        second_digit = i % 10

        # Обчислюємо суму квадратів цифр
        sum_of_squares = first_digit**2 + second_digit**2

        # Перевіряємо, чи ділиться сума квадратів на n без залишку
        if sum_of_squares % n == 0:
            result.append(str(i))

    # Перевіряємо, чи знайшлося хоча б одне число
    if result:
        print(" ".join(result))
    else:
        print("Таких чисел немає")

