tpl = tuple([s for s in input("Строка символов: ").split()])
a = input("Введите искомый символ: ")
start = -1
stop = len(tpl)
for i in range(len(tpl)):
    if tpl[i] == a and start == -1:
        start = i
        continue
    if tpl[i] == a:
        stop = i + 1
        break
newTpl = tpl[start:stop]
if start == -1:
    newTpl = tuple()
print(newTpl)
