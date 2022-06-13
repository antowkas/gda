# Напишите функцию read_last(lines, file), которая
# - открывает файл, абсолютный путь к которому задан аргументом file
# - и возвращает набор последних строк из файла в количестве,
#   заданном аргументом lines, в обратном порядке начиная с последней.

def read_last(lines: int, file: str):
    with open(file, "r", encoding="UTF-8") as f:
        line = [f.readline()]
        while line[-1] != "":
            if len(line) > lines:
                del line[0]
            line.append(f.readline())
    return reversed(line[:-1])


if __name__ == "__main__":
    for line in read_last(6, "gda/7/poem.txt"):
        print(f"{line=}")
