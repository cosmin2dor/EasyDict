import requests
import logging
from bs4 import BeautifulSoup

BASE_URL = "https://www.larousse.fr/dictionnaires/francais-allemand/{keyword}"


def translate(keyword):
    url = BASE_URL.format(keyword=keyword)
    response = requests.get(url)

    if response.status_code != 200:
        logging.error("Translating {} failed with {}".format(keyword, response.status_code))
        logging.debug("Tried getting {}".format(url))
        raise ValueError

    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.find_all(class_="lienarticle2")

    return [word.get_text() for word in words]


if __name__ == "__main__":
    word = translate("baiser")
    print(word)
