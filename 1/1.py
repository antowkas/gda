# Запросите у пользователя ФИО и адрес.
# Выведите на экран сообщения вида: “Здравствуйте, (ФИО). Ваш заказ отправлен по адресу (адрес)“ с полученными данными.
# Фамилия, имя, отчество и адрес должны начинаться с заглавных букв, вне зависимости от того как их ввел пользователь.

fio = input("Введите ФИО: ").title().strip()
adr = input("Введите адрес: ").title().strip()
print(f"Здраствуйте, {fio}. Ваш заказ отправлен по адресу {adr}.")
