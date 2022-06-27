# Напишите функцию складывающих 2 числа.
# В случае, если переданы не числа выведите на экран 'Ожидаемый тип данных — число'.
# Примечание - используйте только стандартные исключения.


def sum_two_nums(a, b):
    try:
        return (a+0) + (b+0)
    except TypeError:
        print("Ожидаемый тип данных — число")


if __name__ == "__main__":
    print(f"{sum_two_nums(0.5, 2) = }")
    print(f"{sum_two_nums(1, -2) = }")
    print(f"{sum_two_nums('1', 2) = }")