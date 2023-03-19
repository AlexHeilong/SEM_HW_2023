# ДЗ к Семинару 6
# Повторение списков
# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
'''
a1 = int(input('Input number a1: '))
d = int(input('Input number d: '))
n = int(input('Input number n: '))
my_list = []
for i in range(n):
    my_list.append(a1 + i * d)
print(my_list)
'''
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
my_list = [random.randint(-10, 10) for i in range(20)]
print(my_list)
max_num = int(input('Input max number: '))
min_num = int(input('Input min number: '))
for i in range(len(my_list)):
    if my_list[i] <= max_num and my_list[i] >= min_num:
        print('индекс', i, '- ' 'значение ', my_list[i])