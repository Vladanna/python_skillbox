import my_math

numbers = list([int(s) for s in input("Введите целых чисел через пробел: ").split(" ")])
answer_question = input("Какую операцию вы хотите сделать? ")

if answer_question == "max":
    my_math.calc_max(numbers)
elif answer_question == "min":
    my_math.calc_min(numbers)
elif answer_question == "middle":
    my_math.calc_middle(numbers)
elif answer_question == "median":
    my_math.cal_median(numbers)
if answer_question == "pstdev":
    my_math.cal_pstdev(numbers)
