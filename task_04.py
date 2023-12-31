"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

n = int(input("Введите целое положительное число: "))

if n < 0:
    print("Вы ввели отрицательное число")
max_num = 0
m = 0
while n > 0:
    m = n % 10
    if m > max_num:
        max_num = m
    n //= 10

print(f"Самая большая цифра в числе - {max_num}")
