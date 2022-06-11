# Есть список list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""].
# Удалите все пустые строки из списка используя lambda функцию.

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]
list1 = filter(lambda x: x != "", list1)
