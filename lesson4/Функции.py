import random
'''
 Синтаксис создания функций
 def(define) название_функции(параметры)
    тело функции

! Правила хорошего тона:
 - Все функции пишутся в верхней части программы
 - Между функциями нужно оставлять две пустые строки
 - 1 функция = 1 действие (не нужно все вставлять в одну функцию)

 Вызов функции
    название_функции(аргументы)
'''

import random


# def print_triangle():
#     print('  *')
#     print(' ***')
#     print('*****')
#
#
# print_triangle()
# print()
#
# print('Задача 1: Вывести hello world столько раз, сколько напишет пользователь')
# def print_hello_world():
#     for _ in range(int(input('Напишите количество раз которое надо вывести: '))):
#         print('hello world!')
#
# print_hello_world()
#
# print()
# print('Задача 2: вывести треугольник который будет размером М на N')
#
# def rectangle():
#     m = int(input('Введите высоту'))
#     n = int(input('Введите длину'))
#
#     for i in range(m):
#         print('*' * n)
# # Данная функция не совсем коректна со стороны хорошего тона, т.к. в ней что-то записывается и выводится
# rectangle()

print('Задача 3: известны оценки 25 учеников. Еть ли среди них двойки? Удалить из списка все отрицательные элементы ')
def marks():
    lst = [random.randint(1,5) for _ in range(25)]
    print(lst)
    if 2 in lst:
         print('есть двойки')

def remove_negative():
    lst = [random.randint(-10, 10) for _ in range(25)]
    print(lst)
    i = 0
    while i < len(lst):
       if lst[i] < 0:
           lst.remove(lst[i])
           i -= 1
       i += 1
    print(lst)

marks()
remove_negative()