from random import randint

'''
Задачи:
1) Написать функцию, которая будет искать и выводить на экран минимальное число, большее 300 и кратное 19.

print('Задача 1: Написать функцию, которая будет искать и выводить на экран минимальное число, большее 300 и кратное 19')

def print_min_more300_multiple19_number(lst, more_then, multiple):
    min_number = lst[0]
    lst_numbers_more_then = []
    lst_numbers_multiples = []
    for i in lst:
        if i < min_number:
            min_number = i
        if i > more_then:
            lst_numbers_more_then.append(i)
        if i % multiple == 0:
            lst_numbers_multiples.append(i)
    print('Минимальное число: ', min_number)
    print('Числа, которые больше', more_then, ': ', lst_numbers_more_then)
    print('Числа, кратные ', multiple, ': ', lst_numbers_multiples )
lst = [randint(200,350)for _ in range(10)]
print(lst)
print_min_more300_multiple19_number(lst, 300, 19)

2) Написать функцию, которая будет обменивать местами первую и последнюю цифру числа N (1234 → 4231).

print('Задача 2: написать ф-ию, которая будет обменивать местами первую и последнюю цифру числа N(1234 4231)')
def swap_numbers(number = 1234):
    str_number = str(number)
    # Проверка на то, чтобы число имело более одной цифры
    if len(str_number) < 2:
        print(str_number)
    else:
        # переменная[x: y] - показывается переменная от индекса х(не включительно) по индекс у(включительно)
        new_str_number = str_number[-1] + str_number[1: -1] + str_number[0]
        print(new_str_number)
swap_numbers()

# Подсказка по работе со строкой
number1 = 1234
number1_str = str(number1)

print(number1_str[0])
print(number1_str[1: 3])  # с первого индекса не включительно по третий включительно
print(number1_str[-1])

3) Написать функцию, которая будет определять, делится ли число N на: 2, 3, 4, 5, ... (без использования оператора % )

print('Написать функцию, которая будет определять, делится ли число N на: 2, 3, 4, 5...(без использования оператора %)')

def division_without_remainder(number_to_be_devised_by = 2, users_number = 4):

    #  С нуля прибавляем число(это наш шаг), если конечное число равно изначальному, значит, число делится
    a = 0
    while a < users_number:
        a += number_to_be_devised_by
    if a == users_number:
        print('Делится')
    else:
        print('Не делится')
division_without_remainder()

4) Написать функцию, которая будет вычислять и выводить на экран значение выражения
N^M без использования оператора возведения в степень (**).

print('Написать функцию, которая будет вычислять и выводить на экран значение выражения '
      'N^M без использования оператора возведения в степень (**)')
def multiplication(number, degree):
    a = 0
    result = 1
    while a < degree:
        result *= number
        a += 1
    print(result)
    
multiplication(2,4)

5) С клавиатуры вводится пять чисел. Для каждого из них вывести,
является ли оно степенью числа 3. Вынести определение степени в функцию.

print('С клавиатуры вводится пять чисел. Для каждого из них вывести, '
      'является ли оно степенью числа 3. Вынести определение степени в функцию.')


def terms(number, degree):
    a = degree
    while degree < number:
        degree *= degree
    if degree == number:
        print(f'Число {number} является степенью {a}')

    else:
        print(f'Число {number} не является степенью {a}')


lst = [int(input('Введите число: ')) for _ in range(5)]
for i in lst:
    terms(i, 5)

6) Реализовать набор функций для работы со списком:
1) Ввод с клавиатуры/инициализация случайными числами (с параметрами).

print('Ввод с клавиатуры/инициализация случайными числами (с параметрами).')
def foo1(count):
      lst = [int(input('Введите число: ')) for _ in range(count)]
      print(lst)

2) Вывод списка на экран (в одну строчку).

print('Вывод списка на экран (в одну строчку).')
def foo2(lst):
      for i in lst:
            print(i, end=' ')
foo2([randint(1,10) for _ in range(5)])

3) Подсчет максимума и минимума (с индексами).

print('Подсчет максимума и минимума (с индексами)')
def foo3(lst):
      print(lst)
      min_number = max_number = lst[0]
      min_index = max_index = 0
      for i in lst:

            if i < min_number:
                  min_number = i
                  a = min_index
            if i > max_number:
                  max_number = i
                  b = max_index
            min_index += 1
            max_index += 1
      print(f'Максимальное число: {max_number} его индекс: {b}')
      print(f'Минимальное число: {min_number} его индекс: {a}')
foo3([randint(1,10) for _ in range(10)])

Второй способ
def foo22(lst):
    a = ' '
    for i in lst:
        a += str(i) + ' '
    print(a)
foo22([randint(1,10) for _ in range(10)])

4) Подсчет количества элементов, равных (больших/меньших) N.

print('Подсчет количества элементов, равных N')
def foo4(lst, n):
    print(lst)
    count = 0
    for i in lst:
        if i == n:
            count += 1
    print(count)
    
foo4([randint(1,5) for _ in range(10)], 5)

5) Добавление элемента К [в конец массива/на N-ю позицию].

print('Добавление элемента К в конец массива')
def foo5(lst, k):
    print(lst)
    lst.append(k)
    print(lst)

foo5([randint(1, 5) for _ in range(10)], 5)

print('Добавление элемента К на N-ю позицию.')
def foo52(lst, k, index):
    print(lst)
    lst.insert(index, k)
    print(lst)
foo52([randint(1,10) for _ in range(10)], 5, 7)

6)  Удаление из списка [последнего/Nго элемента].

print('Удаление из списка последнего элемента.')
def foo6(lst):
    print(lst)
    lst.pop(-1)
    print(lst)

foo6([randint(1,10) for _ in range(10)])

print('Удаление из списка Nго элемента].')
def foo62(lst, index):
    print(lst)
    lst.pop(index)
    print(lst)

foo62([randint(1,10) for _ in range(10)], 5)

7)Сортировка списка по (возрастанию/убыванию). Повторяющиеся — убирать.



8) Найти третий максимум в списке.
9) Сдвинуть все элементы массива на два вправо. Оставшиеся элементы — поставить слева в том же порядке.
10) Вставить K после максимального элемента.


'''
print('Сортировка списка по возрастанию. Повторяющиеся — убирать.')
def foo7(lst):
    print(lst)



foo7([randint(-10, 10) for _ in range(10)])