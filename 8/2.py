# Имеется URL, например: https://www.ozon.ru/search/?from_global=@&sorting=@&text=@. Напишите функцию, которая:
# - принимает в качестве аргументов указанный URL, а также массив со значениями аргументов
# - и возвращает результат запроса по данному URL, в котором параметрам присвоены соответствующие значения из массива.
# *Пример готовой ссылки https://www.ozon.ru/search/?from_global=true&sorting=price&text=d3*

from requests import get
from requests.exceptions import MissingSchema, ConnectionError
from re import findall


def get_res(url: str, values: list):
    url = url.split("/")
    url, keys = "/".join(url[:-1]), findall(r"[?&](.+?)=@", url[-1])
    if len(keys) != len(values):
        return -1
    url = f"{url}/?" + "&".join([f"{keys[i]}={values[i]}" for i in range(len(keys))])

    try:
        res = get(url)
    except MissingSchema:
        return -2
    except ConnectionError:
        return -3
    return res


if __name__ == "__main__":
    print(get_res("https://www.google.com/search?q=@", ["test"]))
