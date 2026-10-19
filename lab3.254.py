d = float(input("Введіть пробіг за перший день: "))
t = float(input("Введіть цільовий сумарний пробіг: "))

total_distance = d    # Сумарний пробіг
current_day_dist = d  # Пробіг за поточний день
days = 1              # Лічильник днів

# Цикл виконується, поки сумарний пробіг не перевищить t
while total_distance <= t:
    days += 1
    current_day_dist *= 1.1        # Збільшуємо щоденний пробіг на 10%
    total_distance += current_day_dist  # Додаємо до сумарного пробігу

# Виводимо результат у потрібному форматі
print(f"{total_distance:.2f} km, {days} days")

