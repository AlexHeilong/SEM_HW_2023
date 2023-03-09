# Task 1
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
"""
num = int(input('Input number: '))

# sum1 = num//100
# print(sum1)
# sum2 = num%10
# print(sum2)
# sum3 = num//10%10
# print(sum3)
# total = sum1 + sum2 + sum3
total = (num//100) + (num%10) + num//10%10
print(total)
"""
#________________________

# Task 2
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
"""
num = int(input('Input quantity of origami: '))
boy = int(num/6)
girl = int(boy*2*2)

if num%6 == 0:
    print(f'Из {num} журавликов Петя и Сережа сделали по {boy}, а Катя {girl}')
else:
    print(f'Не соответствует условиям задачи')
"""
#________________

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
"""
ticket = int(input('Input ticket number: '))
first_half = ticket//100000 + ticket//10000%10 + ticket//1000%10
second_half = ticket//100%10 + ticket//10%10 + ticket%10
# print(first_half)
# print(second_half)
if first_half == second_half:
    print('Ура!!! Счастливый билет!!!')
else:
    print('Печаль(((')
"""

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
"""
first_side = int(input('Введите длину шоколадки: '))
second_side = int(input('Введите ширину шоколадки: '))
sections = int(input('Введите количество долек: '))
if first_side*second_side > sections and (sections%first_side == 0 or sections%second_side == 0):
    print('Можно')
else:
    print('Нельзя')
"""