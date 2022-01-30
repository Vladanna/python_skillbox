n = int(input("Введите количество чисел: "))
lst = list()
b = 0
summ1 = 0
indexZero = 0
for i in range(n):
    a = int(input("Введите число: "))
    lst.append(a)
    b += a
    if a == 0:
        indexZero = lst.index(0)
        summ1 = b
        lst.insert(indexZero, summ1)
        b = 0
lst.insert(indexZero + 2, b)
print(lst)
