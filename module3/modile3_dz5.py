n = int(input("Сколько задолжников: "))
maxSumma = 0
listStr = list()
personDict = dict([input("Введите имя и задолженность (через пробел): ").split() for _ in range(n)])
for i in personDict:
    helloStr = "Здравствуйте, {0}! Ваша задолженность составляет {1} рублей.".format(i, personDict[i])
    print(helloStr)
    summ = int(personDict[i])
    if maxSumma <= summ:
        if maxSumma != summ:
            listStr.clear()
            maxSumma = summ
        listStr.append(helloStr)
nextStep = input("Желаете продолжить? ")
if nextStep == "да":
    for i in range(len(listStr)):
        maxHelloStr = listStr[i]
        print(maxHelloStr[::-1])
