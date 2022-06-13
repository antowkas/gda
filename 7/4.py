# Напишите функцию, которая
# - принимает в качестве аргументов текстовый файл и слово
# - и возвращает количество вхождений данного слова в текст.

from re import findall


def get_number_of_words(file, word: str):
    word = word.lower()
    count = 0
    line = f.readline()
    while line != "":
        count += len(findall(r"\b" + word + r"\b", line.lower()))
        line = f.readline()
    return count


if __name__ == "__main__":
    with open("gda/7/poem.txt", "r", encoding="UTF-8") as f:
        print(get_number_of_words(f, "я"))
