# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
"""
import random
num = int(input('Input number: '))
my_list = [random.randint(1, 100) for i in range(num)]
print((my_list))
digit = input('Input digit to find it: ')
my_list = str(my_list)
print(my_list.count(digit))
"""

# Вторая задача:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков
#
#     Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#     Будем считать, что на вход подается только одно слово, которое содержит либо
#     только английские, либо только русские буквы.
#
#     ноутбук
#     12

en_dict = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
           2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
           4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'],
           8: ['J', 'X'], 10: ['Q', 'Z']}

ru_dict = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
           2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
           3: ['Б', 'Г', 'Ё', 'Ь', 'Я'], 4: ['Й', 'Ы'],
           5: ['Ж', 'З', 'Х', 'Ц', 'Ч'], 8: ['Ш', 'Э', 'Ю'], 10: ['Ф', 'Щ', 'Ъ']}

word = input('Input a word: ')
new_list = []
sum_list = []
for i in word.upper():
    new_list.append(i)
print(new_list)
for i, j in en_dict.items():
    for k in j:
        if k in new_list:
            # print(i, j, k)
            sum_list.append(i)
print(sum_list)
sum = 0
for i in range(len(sum_list)):
    sum += sum_list[i]
print(sum)
print(f'Сумма очков, полученных со слова {word} равна {sum}')

# word = input('Input a word: ')
# new_list = []
# sum_list = []
# for i in word.upper():
#     new_list.append(i)
# print(new_list)
# for i, j in ru_dict.items():
#     for k in j:
#         if k in new_list:
#             print(i, j, k)
#             sum_list.append(i)
# print(sum_list)
# sum = 0
# for i in sum_list:
#     sum += i
# print(sum)
# print(f'Сумма очков, полученных со слова {word} равна {sum}')
