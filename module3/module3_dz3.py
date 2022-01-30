lst = [int(s) for s in input("Строка целых чисел: ").split()]
occur_before = set()
for num in lst:
    if num in occur_before:
        print('Да')
    else:
        print('Нет')
        occur_before.add(num)
