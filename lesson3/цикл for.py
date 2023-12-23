from random import randint


# # range(start, stop, step) - позволяет генерировать последовательности
# range(5)  # 0,1,2,3,4
# range(1, 5, 1)  # 1,2,3,4
# range(10, 1, -1)  # 10,9,8,7,6,5,4,3,2,1
# range(1, 10, 2)  # 1,3,5,7,9
#
#
# print('Задача 1: Вывести hello world 5 раз')
#
# for i in range(5):  # Вместо i(переменной которая не используется) можно написать " _ ", это будет переменная которую не используют
#     print('hello world')
#
#
# print('Задача 2: Пользователь вводит число, оно будет равняться стороне квадрата. Вывести квадрат')
#
# a = int(input('Введите число '))
# for i in range(a):
#     print('* ' * a)
#
# print()
#
# # Списки, в них могут быть разные переменные(булевые, текст, числа, дробные числа)
# lst = [14, 32, True, 'hello world', 15.2]  # Нумерация, как и везде начинается с 0
# print('Вывод списка ', lst[1])
#
# # Можно идти с конца списка, он начинается с -1
# print('Вывод списка с конца[-3] ', lst[-3])
#
# # Можно указывать список в списке
# lst1 = [1.2, 2, 3, [1, 2, 3], 5]
# print('Вывод списка в списке: ', lst1[3][2])
#
# print()
#
# for elem in lst:
#     print(elem)
# print('Конец списка')
#
# print('Вывод всех элементов списка, кроме элемента True')
# # continue - пропуск итерации
# for elem in lst1:
#     if elem == True:
#         continue  # Это значит, что True не выведется
#     print(elem)
#
# print()
#
# print('Пользователь вводит отрезок а, b и шаг step, вывести последовательность в консоль')
#
# a = int(input())
# b = int(input())
# step = int(input())
#
# for i in range(a, b, step):
#     print(i)
#
# print()
#
# print('Даны 2 числа а и b. Вывести в порядке возрастания от а до  b включительно, если a < b, в ином случае, вывести последовательность в порядке убывания')
#
# a1 = int(input())
# b1 = int(input())
#
# if a1 < b1:
#     for i in range(a1, b1 + 1):
#         print(i)
# else:
#     for j in range(a1, b1 - 1, -1):
#         print(j)


# print()
#
# print('Вывести сумму всех нечетных чисел от а до b (включая обе границы)')
#
# a2 = int(input())
# b2 = int(input())
# count = 0
# print('Все числа в списке: ')
#
# for i in range(a2, b2 + 1):
#     if i % 2 != 0:
#         print(i)
#         count += i
# print('Ответ: ', count)


# Методы списка:

# len - длина списка
# lst = [4, 6, 7]
# print(len(lst))  # 3
#
# # Узнать последний эл-т с помощью len
# print(lst[len(lst) - 1])
#
# # добавить объект в конец списка
# lst.append(9)  # 4, 6, 7, 9
# print(lst)
#
# # Удаление элемента. 2 способа
# # del
# del lst[0]  # Удалить 4
#
# # remove. Удалим 9
# if 9 in lst:
#     lst.remove(9)
# else:
#     print("Такого числа нет в списке")


# print('Есть список из 10 элементов, найти сумму элементов этого списка')
# lst = []
# for i in range(10):
#     lst.append(randint(-10, 10))
# print(lst)
# print('-----------------------------------')
#
# count = 0
# for i in lst:
#     count += i
# print(count)
# print()
#
# count1 = 0
# print('Есть список из 10 элементов, посчитать сумму четных цифр в списке')
# for i in lst:
#     if i % 2 == 0:
#         count1 += i
# print(count1)
# print()
#
# print('Есть список из 10 элементов, найти наибольшее и наименьшее число в списке')
# max_num = lst[0]
# min_num = lst[0]
# for i in lst:
#     if i > max_num:
#         max_num = i
#     if i < min_num:
#         min_num = i
# print('Наибольшее число: ', max_num)
# print('Наименьшее число: ' + str(min_num))
# print()
#
# print('Прошлая задача, но нужно найти индекс минимального и максимального элемента в списке')
# index_max_nuber = 0
# index_min_nuber = 0
# s = 0
#
# for i in lst:
#     if i > max_num:
#         max_num = i
#         index_max_nuber = s
#     if i < min_num:
#         min_num = i
#         index_min_nuber = s
#     s += 1
# print('Наибольшее число: ', max_num, ' Его индекс = ', index_max_nuber)
# print('Наименьшее число: ' + str(min_num) + ' Его индекс = ' + str(index_min_nuber))
# print()
#
# # Второй способ
# for index in range(len(lst)):
#     if lst[index] > max_num:
#         max_num = lst[index]
#         index_max_nuber = index
#     if lst[index] < min_num:
#         min_nuber = lst[index]
#         index_min_nuber = index
# print('Наибольшее число: ', max_num, ' Его индекс = ', index_max_nuber)
# print('Наименьшее число: ' + str(min_num) + ' Его индекс = ' + str(index_min_nuber))
# print()
#
#
# # Третий способ
# i = 0
# while i < len(lst):
#     if lst[i] > max_num:
#         max_num = lst[i]
#         index_max_nuber = i
#     if lst[i] < min_num:
#         index_min_nuber = lst[i]
#         index_min_nuber = i
#     i += 1
# print('Наибольшее число: ', max_num, ' Его индекс = ', index_max_nuber)
# print('Наименьшее число: ' + str(min_num) + ' Его индекс = ' + str(index_min_nuber))
# print()
import random

# Создание списков
lst1 = []
for i in range(10):
    lst1.append(random.randint(1, 10))
print(lst1)

'''
Генерация списков
синтакис:
название_переменной = [формула for переменная in range(количество элементов)]
'''

lst = [random.randint(0,10) for i in range(10)]
print(lst)

print('Вывод списка через while ')
#  Чтобы вывести список через while, нужно использовать len(количество элементов)
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
print(lst)
print('Конец списка')
print()
