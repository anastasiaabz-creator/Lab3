while True:
    n = int(input("Введіть n (1 < n <= 100): "))
    if n <= 1 or n > 100:
        print("Число не підходить")
        break
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue
        print(i, end=" ")
    print()

