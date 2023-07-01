"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

number = int(input('Введите номер месяца: '))

# вариант 1
# winner = (12, 1, 2)
# spring = (3, 4, 5)
# summer = (6, 7, 8)
# autumn = (9, 10, 11)
#
# for i in range(len(winner)):
#     if number == winner[i]:
#         print('Зима')
#
# for i in range(len(spring)):
#     if number == spring[i]:
#         print('Весна')
#
# for i in range(len(summer)):
#     if number == summer[i]:
#         print('Лето')
#
# for i in range(len(autumn)):
#     if number == autumn[i]:
#         print('Осень')


# вариант 2
# if number == 1 or number == 2 or number == 12:
#     print(f'{number} - Зима')
#
# elif number == 3 or number == 4 or number == 5:
#     print(f'{number} - Весна')
#
# elif number == 6 or number == 7 or number == 8:
#     print(f'{number} - Лето')
#
# elif number == 9 or number == 10 or number == 11:
#     print(f'{number} - Осень')

# вариант 3
year = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

for i, month in year.items():
    if number in month:
        print(i)

