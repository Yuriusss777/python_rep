"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

revenue = int(input("Введите вырочку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

if revenue > costs:
    print(f"Прибыль компании оставила  = {revenue - costs}")
    print(f"Рентабельность выручки составила = {(revenue - costs) / revenue}")
elif revenue == costs:
    print("Прибыли и убытка у компании нет")
else:
    print(f"убыток компании составил = {costs - revenue}")

number_employees = int(input("Введите количество сотрудников фирмы: "))
print(f"Прибыль фирмы в расчете на одного сотрудника = {(revenue - costs) / number_employees}")
