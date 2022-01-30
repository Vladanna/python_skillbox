date = int(input("Введите число: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
if date == 31 and (month == 2 or month == 4 or month == 6 or month == 9 or month == 11):
    print("Даты не существует")
elif date == 29 and month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("Дата существует")
elif (date == 29 or date == 30) and month == 2:
    print("Даты не существует")
elif 0 < date <= 31 and 1 <= month <= 12 and 0 <= year <= 9999:
    print("Дата существует")
else:
    print("Дата не существует")

