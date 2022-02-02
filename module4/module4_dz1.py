hours = int(input("Введите количество часов: "))


def is_night():
    message = "Сейчас ночь"
    return message


def is_morning():
    message = "Сейчас утро"
    return message


def is_day():
    message = "Сейчас день"
    return message


def is_evening():
    message = "Сейчас вечер"
    return message


def setup_time():
    if 0 <= hours <= 5:
        return is_night()
    elif 6 <= hours <= 11:
        return is_morning()
    elif 12 <= hours <= 17:
        return is_day()
    elif 18 <= hours <= 23:
        return is_evening()
    else:
        a = "Данные неккоретны"
        return a


print(setup_time())
