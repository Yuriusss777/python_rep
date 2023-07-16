"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

PERCENTAGES = 100


def salary_calculation(*args):
    prize_new = int(production) * int(bet) / int(PERCENTAGES) * int(prize)
    salary = int(production) * int(bet) + prize_new

    return salary


script_name, production, bet, prize = argv

print(f'Заработная плата сотрудника составляет: {salary_calculation(argv)}')
