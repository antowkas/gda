# Есть список lst = [10, 17, 13, 44, 23, 88, 100, 99].
# Напишите программу которая пробегается по списку и выводит экран только четные числа.
# Так же напишите вариант, который выводит только нечетные числа.

lst = [10, 17, 13, 44, 23, 88, 100, 99]

print("Чётные числа:", end=" ")
for el in lst:
    if el%2 == 0:
        print(el, end=" ")

print("\nНечётные числа:", end=" ")
for el in lst:
    if el%2 != 0:
        print(el, end=" ")
