import requests
import logging
from bs4 import BeautifulSoup

BASE_URL = "https://hallo.ro/dictionar-francez-roman/{keyword}"


def translate(keyword):
    url = BASE_URL.format(keyword=keyword)
    response = requests.get(url)

    if response.status_code != 200:
        logging.error("Translating {} failed with {}".format(keyword, response.status_code))
        logging.debug("Tried getting {}".format(url))
        raise ValueError

    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.find_all(class_="right")

    # Skip first entry as it indicates the language
    return [word.get_text().strip() for word in words[1:]]


if __name__ == "__main__":
    word = translate("baiser")
    print(word)
