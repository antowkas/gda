# Напишите функцию, которая
# - принимает URL
# - и возвращает код статуса, полученный в ответе на GET-запрос по данному URL, а также сам URL.

from requests import get
from requests.exceptions import MissingSchema, ConnectionError


def get_status(url: str):
    try:
        res = get(url)
    except MissingSchema:
        return -1, url
    except ConnectionError:
        return -2, url
    return res.status_code, url


if __name__ == "__main__":
    status, url = get_status("http://google.com")
    print(f"{status=}\n{url=}")
