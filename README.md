# Курс 2. Курсовая работа

Позади самые важные 9 недель обучения, теперь вас ждет подготовка к собеседованию. Необходимо выполнить курсовую работу, чтобы проверить и показать свои знания. Курсовой проект — это точно такое же домашнее задание, его точно так же проверит наставник, просто это задание финальное.

<aside>
💡 ВАЖНО! Сначала **изучить материалы всех пройденных уроков**, а только потом приступать к выполнению курсовой работы.

</aside>

Мы снова пишем игру, на этот раз — в слова. Сыграйте в [игру на сайте Яндекса](https://yandex.ru/games/play/99195), чтобы понять общий принцип.

## Пример работающего приложения

```python

**Программа:** Ввведите имя игрока
**Пользователь:** Василий 

**Программа:** Привет, Василий!
**Программа:** Составьте 8 слов из слова ПИТОН
**Программа**: Слова должны быть не короче 3 букв
**Программа**: Чтобы закончить игру, угадайте все слова или напишите "stop"
**Программа**: Поехали, ваше первое слово?

**Пользователь:** пони
**Программа:** верно

**Пользователь:** патефон
**Программа:** неверно

**Пользователь:** ион
**Программа:** верно

**Пользователь:** опт
**Программа:** верно

**Пользователь:** пот
**Программа:** верно

**Пользователь:** тип
**Программа:** верно

**Пользователь:** топ
**Программа:** верно

**Пользователь:** пион
**Программа:** верно

**Пользователь:** понт
**Программа:** верно

**Программа:** Игра завершена, вы угадали 8 слов!

****(программа завершена)
```

```python
**Программа:** Ввведите имя игрока
**Пользователь:** Василий 

**Программа:** Привет, Василий!
**Программа:** Составьте 8 слов из слова ПИТОН
**Программа**: Слова должны быть не короче 3 букв
**Программа**: Чтобы закончить игру, угадайте все слова или напишите "stop"
**Программа**: Поехали, ваше первое слово?

**Пользователь:** руна
**Программа:** верно

**Пользователь:** стоп
**Программа:** Игра завершена, вы угадали 1 слов!

****(программа завершена)
```

Инструкция дальше разбита на шаги, выполните их последовательно.

### Шаг 0

Запишите данные в формате:

```python
[{
    "word": "питон",
     "subwords":  [
         "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
     ]},
    {
      "word": "набор",
      "subwords":  [
          "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
     ]},
    {
			"word": "строка",
			"subwords": [
         "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора", 
         "коса", "сота", "торс", "роса", "скат"
     ]
}]
```

```python
Больше слов можно взять здесь:

https://wordhelp.ru/comb/%D0%BD%D0%B0%D0%B1%D0%BE%D1%80 
```

Разместите список слов на внешнем ресурсе, например, https://jsonkeeper.com/. Чтобы разместить список, откройте ссылку в браузере,  скопируйте JSON в текстовое поле, нажмите save, скопируйте ссылку в верху экрана. Это и будет путь, по которому хранится JSON. Если у вас возникают ошибки при работе с jsonkeeper (сервис может быть не доступен), для размещения json на внешнем ресурсе используйте аналог сервиса - [npoint](https://www.npoint.io/).

![2022-05-05 13.25.19.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0116aa6-008d-411e-93bb-2ae04286f71b/2022-05-05_13.25.19.gif)

### Шаг 1

Создайте класс `BasicWord` в отдельном файле. Этот класс будет содержать в себе:

**Поля:**

- исходное слово,
- набор допустимых подслов.

**Методы:**

- проверку введенного слова в списке допустимых подслов (вернет bool),
- подсчет количества подслов (вернет int).

Не забудьте определить метод  `__repr__`

**При инициализации** экземпляру задаются: **исходное слово** и набор **допустимых слов,** составленных из исходного. ****

### Шаг 2

Создайте класс `Player`. Этот класс будет содержать в себе:

**Поля:**

- имя пользователя,
- использованные слова пользователя.

**Методы:**

- получение количества использованных слов (возвращает int);
- добавление слова в использованные слова (ничего не возвращает);
- проверка использования данного слова до этого (возвращает bool).

Не забудьте определить метод  `__repr__`

### Шаг 3

Напишите функцию `load_random_word()` в файле `utils`, которая:

- получит список слов с внешнего ресурса,
- выберет случайное слово,
- создаст экземпляр класса `BasicWord`,
- вернет этот экземпляр.

<aside>
💡 Подготовительные шаги завершены, теперь мы пишем основной код программы.

</aside>

### Шаг 4

Напишите стартовую логику: приветствие и вывод слова:

- Импортируйте нужные классы и функции.
- Получите у пользователя его имя.
- Создайте экземпляр класса Player с нужным именем.
- Поздоровайтесь с пользователем.
- Выведите значение слова из экземпляра, который вы получили ранее из `load_random_word`.
- Предложите сделать первый ход.

```python
**Программа:** Ввведите имя игрока
**Пользователь:** Василий 

**Программа:** Привет, Василий!
**Программа:** Составьте 8 слов из слова ПИТОН
**Программа**: Слова должны быть не короче 3 букв
**Программа**: Чтобы закончить игру, угадайте все слова или напишите "stop"
**Программа**: Поехали, ваше первое слово?
```

### Шаг 5

Запускайте цикл, пока количество угаданных слов не сравняется с количеством слов, которые можно составить.

В каждой итерации получите от пользователя слово, выполните несколько проверок:

- Если слово короче 3 букв – это неудачное слово.

```python
**Пользователь:** мя
**Программа:** слишком короткое слово
```

- Если слова нет в списке допустимых у BasicWord – это неудачное слово.

```python
**Пользователь:** ъуъ
**Программа:** неверно
```

- Если слово уже было угадано пользователем (Player) – это неудачное слово.

```python
**Пользователь:** руна
**Программа:** уже использовано
```

- Если слово `stop` или `стоп`, то игра прекращается.

```python
**Пользователь:** стоп
**Программа:** (выводит статистику, см шаг 6)
```

Если все проверки выше пройдены, то слово хорошее, его нужно добавить слово в список использованных слов класса Player и вывести оповещение об этом пользователю:

```python
**Пользователь:** руна
**Программа:** верно
```

### Шаг 6

Выведите количество угаданных слов. Информацию получите из экземпляра класса Player. 

```python
**Программа:** Игра завершена, вы угадали 8 слов!
```

### Шаг 7

Когда всё готово, протестируйте программу, проверьте свой стиль кода, соответствие требованиям, исправьте ошибки, которые показывает PyCharm, запакуйте файл (или файлы) в ZIP-архив и сдайте на платформу.

### Подсказки

Структура вашего проекта может выглядеть так:

```python
main.py          – это основной файл приложения

players.py       - тут класс игрока
basic_word.py    - тут класс слова

utils.py         - тут лежат функции

```

### Критерии проверки работы

- [ ]  Используются объекты.
- [ ]  У классов Player , BasicWord реализован `__repr__`
- [ ]  Получение данных реализовано в виде функции.
- [ ]  Функции и классы вынесены в отдельные файлы.
- [ ]  Данные загружаются с помощью requests.