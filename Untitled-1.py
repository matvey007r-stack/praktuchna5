
n = int(input("Введіть кількість чисел N: "))

if n <= 0:
    print("Помилка! N повинно бути більшим за 0.")
else:
    total = 0
    count = 0

    minimum = None
    maximum = None

    for i in range(n):
        number = float(input(f"Введіть число {i + 1}: "))

        total += number

        if minimum is None or number < minimum:
            minimum = number

        if maximum is None or number > maximum:
            maximum = number

        if number > 5:
            count += 1

    average = total / n

    print("\nРезультати:")
    print("Сума:", total)
    print("Середнє:", average)
    print("Мінімум:", minimum)
    print("Максимум:", maximum)
    print("Чисел > 5:", count)
