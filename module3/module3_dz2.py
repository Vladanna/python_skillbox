n = int(input("Сколько записей в словаре: "))
lst = {}
lstNonZero = list()
summBalance = 0
for i in range(n):
    key = int(input("Номер счета: "))
    lst[key] = int(input("Сумма: "))
    if lst[key] < 0:
        lstNonZero.append(key)
        lst.pop(key)
    else:
        summBalance += lst[key]

print("Счета с отрицательным балансом: ", lstNonZero)
print("Общая сумма на счетах с положительным балансом: ", summBalance)
