n = int(input("Введите число n: "))
i = 1
b = 0
maxN = 0
minN = 0
while i <= n:
    a = int(input("Введите число: "))
    if i == 1:
        maxN = a
        minN = a
    elif a >= maxN:
        maxN = a
    elif a < minN:
        minN = a
    i += 1
    b += a
summ = int(b / n)

print("Максимасильное число", maxN)
print("Минимальное число", minN)
print("Среднее арифмитическое", summ)
