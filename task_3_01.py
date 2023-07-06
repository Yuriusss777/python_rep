"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def my_func(num_1, num_2):
    if num_2 == 0:
        try:
           res = num_1 / 0
        except ZeroDivisionError:
            return print('Вы что? Пытаетесь делить на 0!')
    res = num_1 / num_2
    return res


print(my_func(float(input("Укажите первое число: ")), float(input("Укажите второе число: "))))
