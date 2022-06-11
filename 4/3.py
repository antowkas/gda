# Есть список list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""].
# Удалите все пустые строки из списка.

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]
print(f"До: {list1}")
for i in range(list1.count("")):
    list1.remove("")
print(f"После: {list1}")