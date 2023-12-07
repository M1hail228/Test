# Если текст умножить на число, то тогда оно будет дублироваться
x = 'la'*3
print(x)

# Работа с input
x = int(input())

if x == 52:
    print('Писятдва')
elif x < 5 or x > 10:
    print('Хороший выбор')
else:
    print('Плохой выбор')

# Объединение текста
a = 'How are you '
b = 52
c = ' Да здравствует Санкт-Петербург и этот город наш'

print(a + str(b) + c)


# Дано трёхзначное число. Определить, есть ли среди его цифр одинаковые
number = 455
for compare in str(number):
    if str(number).count(compare):
        print('Есть одинаковые числа')
        break
    else:
        print('Нет одинаковых чисел')
