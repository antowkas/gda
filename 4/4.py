# Есть список с повторяющимися элементами (составьте сами).
# Удалите из него все повторы.

lst = [1, 2, 3, 1, 3, 2, 4, 4, 5, 6, 7, 7, 8, 1, 2, 3, 8]
print(f"До: {lst}")
length, i = len(lst), 0
lst = list(reversed(lst))
while i < length:
    el = lst[i]
    for _ in range(1, lst.count(el)):
        length -= 1
        lst.remove(el)
    i += 1
lst = list(reversed(lst))
print(f"После: {lst}")
