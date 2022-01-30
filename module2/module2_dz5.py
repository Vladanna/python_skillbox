import math
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число с: "))

d = b ** 2 - 4 * a * c

if d < 0:
    print("Корней нет")
elif d > 0:
    x1 = ((-b) + math.sqrt(d)) / (2 * a)
    x2 = ((-b) - math.sqrt(d)) / (2 * a)
    print("Два корня x1=", int(x1), "x2=", int(x2))
else:
    x = ((-b) + math.sqrt(d)) / (2 * a)
    print("Один корень x=", int(x))
