# Создайте переменную password в которой хранится пароль.
# Запрашивайте у пользователя ввести пароль до тех пор пока он не напишет правильно или не введет символ ‘q’.

password = "Admin1"
inp = None
while inp != password and inp != "q":
    inp = input("Введите пароль: ")