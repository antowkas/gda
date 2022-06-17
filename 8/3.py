# Напишите функцию, которая
# получает в качестве аргумента список языков программирования ['python', 'c++', 'java', 'javascript', 'ruby', 'c#']
# и возвращает массив, в котором каждый элемент является списком, состоящим из названия языка программирования
# и количества репозиториев на GitHub, в которых применяется данный язык программирования.

from requests import get


def get_rep(languages: list[str]) -> list[tuple[str, int]]:
    out = []
    for language in languages:
        res = get("https://api.github.com/search/repositories?q=language:" + language).json()
        if "errors" in res:
            out.append((language, -1))
        else:
            out.append((language, res["total_count"]))
    return out


if __name__ == "__main__":
    print(get_rep(['python', 'c++', 'java', 'javascript', 'ruby', 'c#']))
