one_number = int(input("Введите первое число: "))
two_number = int(input("Введите втрое число: "))
symbol_operation = input("Введите операцию: ")


def execute(first_number, second_number, operation):
    if operation == "+":
        thirdNumber = first_number + second_number
    elif operation == "-":
        thirdNumber = first_number - second_number
    elif operation == "*":
        thirdNumber = first_number * second_number
    elif operation == "/":
        thirdNumber = first_number / second_number
    else:
        thirdNumber = "Данные неккоретны"
    return thirdNumber


print(execute(one_number, two_number, symbol_operation))
