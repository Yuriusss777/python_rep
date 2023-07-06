"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# def my_func(*args):
#     my_list = []
#     for i in args:
#         my_list.append(i)
#     my_list.sort()
#     sum_max_el = my_list[-1] + my_list[-2]
#     return sum_max_el
#
#
# print(my_func(15, 25, 100))

def my_func(*args):
    """без метода sort"""
    if args[0] > args[1] > args[2]:
        sum_max_el = args[0] + args[1]
    elif args[0] > args[1] < args[2]:
        sum_max_el = args[0] + args[2]
    else:
        sum_max_el = args[1] + args[2]

    return sum_max_el


print(my_func(10, 15, 100))
