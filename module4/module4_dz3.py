numbers = list([float(s) for s in input("Введите набор чисел с плавающей точкой через запятую: ").split(",")])
answer_question = input("Желаете ввести самостоятельно точность округления? ")
list_final = list()


def calculate_round(number, pows=2):
    return round(number, pows)


if answer_question == "да":
    pow_round = int(input("Введите стенепь округления: "))
    for i in range(len(numbers)):
        list_final.append(calculate_round(numbers[i], pow_round))
else:
    for i in range(len(numbers)):
        list_final.append(calculate_round(numbers[i]))

print(list_final)
