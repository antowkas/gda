# Напишите функцию, которая
# - в качестве аргумента принимает текстовый файл
# - и возвращает самое длинное слово из файла (если таких слов несколько, то выводит их список).

from re import findall


def get_longest(file):
    longest_word = [""]
    longest_word_num = 0
    line = f.readline()
    while line != "":
        words = findall(r"\b\w+\b", line)
        for word in words:
            num = len(word)
            if num == longest_word_num:
                longest_word.append(word)
            elif num > longest_word_num:
                longest_word = [word]
                longest_word_num = num
        line = f.readline()
    if len(longest_word) == 1:
        longest_word, = longest_word
    return longest_word


if __name__ == "__main__":
    with open("gda/7/poem.txt", "r", encoding="UTF-8") as f:
        print(get_longest(f))
