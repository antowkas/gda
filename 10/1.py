# Напиште собственное исключение с сообщением 'Имя не может содержать в себе цифры'.
# Напишите функцию check_name, которая выводи переданное имя на экран, если в нем нет цифр,
# либо вызывает срабатывание написанного вами исключения, если в имени присутствуют цифры.
# Примечание - подразумеваются числа в строчном типе данных, например, '7'.

from re import match


class NameContainNumber(Exception):
    def __init__(self, text):
        self.text = text


def check_name(name):
    if match(r".*\d", name):
        raise NameContainNumber("Имя не может содержать в себе цифры")
    else:
        print(name)


if __name__ == "__main__":
    check_name("Ivan Goncharov")
    check_name("PythonMage1")
