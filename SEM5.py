# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
'''
def recursion(a, b):
    if b == 0:
        return 1
    return a * recursion(a, b - 1)

a = int(input('Input a: '))
b = int(input('Input b: '))
print(recursion(a, b))
'''

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def recOfSum(a, b):
    if b == 0:
        return a
    return 1 + recOfSum(a, b -1)
a = int(input('Input a: '))
b = int(input('Input b: '))
print(recOfSum(a,b))