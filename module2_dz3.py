n = int(input("Введите натуральное число N: "))
i = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i ** 2)
