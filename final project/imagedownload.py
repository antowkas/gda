# Python 3.9

import time
import asyncio
from requests import get
from bs4 import BeautifulSoup
from re import match, search as search
import shutil


class StatusCode(Exception):
    def __init__(self, text):
        self.text = text


def get_img_urls_from_url(url: str) -> str:
    """Ищет картинки из url"""
    res = get(url)
    if (status_code := res.status_code) != 200:
        raise StatusCode(f"The status code 200 was expected, but {status_code} was received")
    soup = BeautifulSoup(res.text, 'html.parser')
    img_tags = soup.find_all('img')
    for i in range(len(img_tags)):
        img_url: str = img_tags[i]['src']
        if match(r".*\.(png|jpg|gif|jpeg|bmp|pcx|raw|svg)$", img_url.lower()[-4:]):
            if img_url[0] == "/":
                pattern = r"(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b)"
                main_url = search(pattern, url).group(0)
                img_url = main_url + img_url
            yield img_url


async def download_image_from_url(image_url: str, filename: str) -> None:
    """Скачивает картинку в файл из url"""
    res = get(image_url, stream=True)
    if (status_code := res.status_code) != 200:
        raise StatusCode(f"The status code 200 was expected, but {status_code} was received")
    res.raw.decode_content = True
    with open(filename, 'wb') as file:
        print(f"Запись {filename}")
        shutil.copyfileobj(res.raw, file)


async def download_images_from_url(url: str) -> None:
    """Скачивает все картинки из url в файлы"""
    tasks = list()
    for i, img_url in enumerate(get_img_urls_from_url(url)):
        filename = f"{i}.{img_url.split('.')[-1]}"
        print(f"Найден ({img_url}) ({filename})")
        tasks.append(asyncio.create_task(download_image_from_url(img_url, filename)))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(download_images_from_url("https://stopgame.ru/news"))
