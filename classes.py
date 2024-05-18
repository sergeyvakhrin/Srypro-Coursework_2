class BasicWord():
    """
    **Поля:**
    - исходное слово,
    - набор допустимых подслов.
    **Методы:**
    - проверку введенного слова в списке допустимых подслов (вернет bool),
    - подсчет количества подслов (вернет int).
    """
    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = subwords
        self.user_word = None

    def __repr__(self):
        return f'Слово: {self.word}. Варианты слов {self.subwords}. Введенное слово: {self.user_word}'

    def is_correct_subword(self) -> bool:
        """
        - проверку введенного слова в списке допустимых подслов (вернет bool),
        """
        return self.user_word in self.subwords

    def counter_subwords(self) -> int:
        """
        - подсчет количества подслов (вернет int).
        """
        return len(self.subwords)


class Player():
    """
    **Поля:**
    - имя пользователя,
    - использованные слова пользователя.
    **Методы:**
    - получение количества использованных слов (возвращает int);
    - добавление слова в использованные слова (ничего не возвращает);
    - проверка использования данного слова до этого (возвращает bool).
    """
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.user_subwords = []
        self.user_word = None

    def __repr__(self):
        return f'Имя: {self.user_name}. Введенные слова: {self.user_subwords}'

    def get_count_words(self) -> int:
        """
        - получение количества использованных слов (возвращает int);
        """
        return len(self.user_subwords)

    def get_word_use(self) -> None:
        """
        - добавление слова в использованные слова (ничего не возвращает);
        """
        return self.user_subwords.append(self.user_word)

    def is_use_word(self) -> bool:
        """
        - проверка использования данного слова до этого (возвращает bool).
        """
        return self.user_word in self.user_subwords




