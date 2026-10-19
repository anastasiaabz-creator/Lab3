a = int(input("Введіть число: "))
b = int(input("Введіть число: "))

# Шукаємо найбільший спільний дільник (НСД)
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

# НСК = (a * b) / НСД
print(a * b // gcd)

