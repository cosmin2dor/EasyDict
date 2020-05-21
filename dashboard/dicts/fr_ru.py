import requests
import logging
from bs4 import BeautifulSoup

BASE_URL = "https://www.multitran.com/m.exe?l1=4&l2=2&s={keyword}"


def translate(keyword):
    url = BASE_URL.format(keyword=keyword)
    response = requests.get(url)

    response.encoding = 'utf-8'

    if response.status_code != 200:
        logging.error("Translating {} failed with {}".format(keyword, response.status_code))
        logging.debug("Tried getting {}".format(url))
        raise ValueError

    soup = BeautifulSoup(response.text, 'html.parser')
    lines = soup.find_all(class_="trans")

    words = []

    for line in lines:
        [words.append(word) for word in line.get_text().split(';')]

    return words


if __name__ == "__main__":
    word = translate("baiser")
    print(word)
