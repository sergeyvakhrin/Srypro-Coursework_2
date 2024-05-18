from classes import Player
from utils import load_random_word


def main():
    """
    Логика программы
    """
    basicword = load_random_word()

    user_name: str = input("Введите имя игрока: ")
    player = Player(user_name)

    basicword_counter_subwords = basicword.counter_subwords()
    basicword_word = basicword.word

    print(f'Привет, {user_name}!\n'
            f'Составьте {basicword_counter_subwords} слов из слова {basicword_word.upper()}\n'
            f'Слова должны быть не короче 3 букв\n'
            f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
            f'Поехали, ваше первое слово? \n')

    while player.get_count_words() != basicword_counter_subwords:
        user_word: str = input().lower().strip()

        player.user_word = user_word
        basicword.user_word = user_word

        if user_word.lower().strip() == "stop" or user_word.lower().strip() == "стоп":
            break
        elif player.is_use_word():
            print("Такое слово уже было.\n")
            continue
        elif basicword.is_correct_subword():
            player.get_word_use()
            print("Верно\n")
        else:
            print("Не верно\n")
            continue

    print(f'Игра завершена, вы угадали {player.get_count_words()} слов!\n')
    print("(программа завершена)")



if __name__ == '__main__':
    main()
