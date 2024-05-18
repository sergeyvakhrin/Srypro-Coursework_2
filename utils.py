import random
from importlib.resources import read_text

import requests
import urllib3

from classes import BasicWord
from settings import URL, WORDS_PATH, game_words


def load_random_word():
    """
    - получит список слов с внешнего ресурса,
    - выберет случайное слово,
    - создаст экземпляр класса `BasicWord`,
    - вернет этот экземпляр.
    """
    urllib3.disable_warnings()
    game_words: list[dict] = requests.get(URL, verify=False).json()

    # game_words: list[dict] = read_text(WORDS_PATH, encoding="UTF-8")

    random.shuffle(game_words)

    return BasicWord(**game_words[0])

