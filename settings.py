from pathlib import Path

URL = "https://jsonkeeper.com/b/5AYT"

ROOT_PATH = Path(__file__).parent
WORDS_PATH = ROOT_PATH.joinpath("data", "words.json")

game_words = [
    {
        "word": "питон",
        "subwords": [
            "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
        ]},
    {
        "word": "набор",
        "subwords": [
            "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
        ]},
    {
        "word": "строка",
        "subwords": [
            "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора",
            "коса", "сота", "торс", "роса", "скат"
        ]}
]

