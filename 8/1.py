# Напишите функцию, которая
# - принимает URL
# - и возвращает код статуса, полученный в ответе на GET-запрос по данному URL, а также сам URL.

from requests import get
from requests.exceptions import MissingSchema


def get_status(URL: str):
    try:
        res = get(URL)
    except MissingSchema:
        return -1, URL
    return res.status_code, URL


if __name__ == "__main__":
    status, url = get_status("http://google.com")
    print(f"{status=}\n{url=}")
