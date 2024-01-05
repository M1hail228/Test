from random import randint
# s1 = 'abc'
# l1 = ['a', 'b', 'c']
# #  Отличие в том, что строки нельзя поменять, как список
#
#
# #  Узнать длину строки
# s = 'abc'
# print(len(s))
#
# #  Перенос строки \n, табуляция \t
# print('Привет, \n Коля и \n \t Дима')
#
# #  Сравнение строк подразумевает собой сравнение номера символов
# print('abc' > 'ac')  # False, так как с имеет большее значение чем b, когда один символ больше другого, сравнение заканчивается
#
# # В тройные ковычки можно писать любые ковычки
# """ Он сказал,"Привет", He's a doctor """
#
# # f - строки
# # С помощью f-строк можно вписывать переменную в текст
# a = 123
# print(f'Мое любимое число: {a}')
#
# #  Перенос строки осуществляется с помощью слэша \
# str = 1 + 1 + 2 + 4 + 5 \
#     + 3 + 7 + 6
#
# #  Индексы в строке. СТРОКИ НЕИЗМЕНЯЕМЫ КАК СПИСКИ!!!!
# str1 = 'qwerty'
# print(str1[0])  # q
# print(str1[1])  # w
# print(str1[-1])  # y
# print(str1[-2])  # t
#
# # Срезы
# word = 'hello'
# #  print(word[start(указываем начальный символ включительно):stop(указываем конечный символ не вкл:step(указываем шаг)])
# print(word[1:4])  # ell
# print(word[:])  # hello
# print(word[::2])  # hlo
# print(word[::-1])  # olleh
#
# # Строки можно перебирать через списки
# word = 'qwerty'
# for char in word:
#     print(char)
#
# print('Задача: написать программу, которая сможет подсчитать как часто встречается в строке введенный символ. Ответ в %')
# word = 'qwertyy'
# desired_letter = input('Введите букву: ')
# counter = 0
# for i in word:
#     if i == desired_letter:
#         counter += 1
#
# print(counter / len(word) * 100, '%')


# РЕШЕНИЕ ПРАКТИКИ
'''
1 уровень:
1) Паша очень любит кататься на общественном транспорте,
а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с
суммой последних трех цифр номера билета.
Программа должна выводить “Счастливый” или “Обычный”.  (Решить с помощью индексов строк, то есть без математики 🥳)
def check_ticket(ticket):
    print(ticket)
    ticket1 = str(ticket)
    if int(ticket1[0]) + int(ticket1[1]) + int(ticket1[2]) == int(ticket1[3]) + int(ticket1[4]) + int(ticket1[5]):
        print('Счастливый')
    else:
        print('Несчастливый')
check_ticket(123006)
2) Дана последовательность символов. Проверить, является ли она палиндромом (слово или текст, одинаково читающееся в обоих направлениях)
word = 'потоп' # input('Введите слово для проверки: ')
reversed_word = word[::-1]
if reversed_word == word:
    print('Является')
else:
    print('Не является')
3) Написать функцию проверки email (представьте, что для своего сайта эту функцию пишете. Сделать проверки, которые считаете нужными, а я буду пробовать сломать)
def check_email(user_email):
    if user_email.count('@') > 1 and user_email.count('.') == 1:
        email_parts = user_email.split('@')
        if not email_parts[0].issalnum():
            return False
        domen_parts = email_parts[1].split('.')
        if not domen_parts[0].issalpha() or not domen_parts[1].issalpha():
            return False
        return True
    return False
print(check_email('mishapetrov470@gmail.com'))
4) Определить количество слов в строке.
Вводится строка, состоящая из слов, разделенных пробелами.
Требуется посчитать количество слов в ней.
s = 'hello world beautiful nice'
print(s.split())
print(len(s.split()))

s1 = 'hello  world  '
words = s1.split(' ')
print(words)
count_word = 0
for word in words:
    if len(word) > 0:
        count_word += 1
print(count_word)

2 уровень:
1) Определить сложность пароля (сделать функцию как на обычных сайтах. То есть проверять большие буквы, символы, цифры И так далее. Подсказка: ascii)
def check_password(password):
    # Будет использована таблица
    lower_case = 0
    upper_case = 0
    numbers = 0
    characters = 0
    for char in password:
        if ord(char) in range(97, 123):
            lower_case += 1
        if ord(char) in range(65, 91):
            upper_case += 1
        if ord(char) in range(48, 58):
            numbers += 1
        if ord(char) in range(33,48) or ord(char) in range(58,65):
            characters += 1
    if len(password) >=12 and \
        lower_case >= 4 and \
        upper_case >= 1 and \
        characters >= 1:
        print('Сложный пароль')

    if len(password) >= 1 and lower_case >=4:
        print('Средний пароль')
check_password('1dfgdf@gfd3sdfgs23H')
2) Необходимо написать программу, которая сможет посчитать повторяющиеся символы и вывести сокращенную строку, пример:
Вход: s = 'aaaabbcaa'
Выход: 'a4b2c1a2'

s = 'aaaaadddssssdfggrehhdfeee'
new_s = ''
i = 0
while i < len(s):
    char = s[i]
    new_s += char
    count = 0
    while i < len(s) and s[i] == char:
        count += 1
        i += 1
    new_s += str(count)
print(new_s)


3) На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в нем.
Пробелы нужно игнорировать (не учитывать при подсчете).
Для выведения результатов вычислений требуется написать функцию top3(st).
Итог работы функции представить в виде строки: «символ – количество раз, символ – количество раз…».
def top3use_symbols(text):
    chars = [0 for i in range(1000)]
    count = [0 for i in range(1000)]
    for char in text:
        chars[ord(char)] = char
        count[ord(char)] += 1

    for i in range(len(chars)):
        if chars[i] != 0:
            print(f'{chars[i]}: {count[i]}')



top3use_symbols('kdjklsddjkldf dfgdfjgjf dfhjg;kljg fjdlgkjs dfjlgjs jdflgjs ururelw ')
4) Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно.
Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок.
s = 'ура руа втавы (врыпжвы) врпвыж'
new_s = ' '
in_brackets = False
for char in s:

    if char == '(':
        in_brackets = True
        continue
    elif char == ')':
        in_brackets == False
        continue
    if in_brackets:
        continue
    new_s += char
print(new_s)

# Решение в следующем файле
УРОВЕНЬ ПСиИииХ : (https://media3.giphy.com/media/1guRIRKAgaEOneVda2Q/giphy.gif?cid=ecf05e4776fhaulj9ulwy8eyhtbnbnh3757ndyj30s0yula9&rid=giphy.gif&ct=g)
1) Взять файл (https://t.me/c/1890650000/15) из закрепа (там html код таблицы с CoinGecko (https://www.coingecko.com/ru) ~5.5к строк)
2) засунуть этот код в переменную (просто скопировать и засунуть в переменную с помощью тройных кавычек)
3) Вывести все названия криптовалют, которые есть  в этом коде (по сути первая страница coingecko - топ 100)
P.S. - не пытайтесь читать код coingecko. Откройте консоль разработчика и найдите закономерности
Подсказка: возле каждого названия криптовалюты есть классы "py-0 coin-name cg-sticky-col cg-sticky-third-col px-0" ориентируйтесь на них, когда будете парсить
'''

