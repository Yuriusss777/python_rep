"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант с LC и с генератором
"""

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# обычный путь
"""
lst_new = []
if len(lst) % 2 == 0:
    for i in range(1, len(lst), 2):
        if lst[i] > lst[i + 1]:
            lst_new.append(lst[i])
        elif lst[i] == lst[i + 1]:
            continue
        else:
            lst_new.append(lst[i + 1])

for i in range(1, len(lst), 2):
    if lst[i] > lst[i + 1]:
        lst_new.append(lst[i])
    elif lst[i] == lst[i + 1]:
        continue
    else:
        lst_new.append(lst[i + 1])

print(lst_new)
"""

# LC
"""
lst_new = [lst[i] if lst[i] > lst[i + 1] else lst[i + 1] for i in range(1, len(lst), 2)]

print(lst_new)
"""

# Генератор

generator = (lst[i] if lst[i] > lst[i + 1] else lst[i + 1] for i in range(1, len(lst), 2))
print(generator)

for el in generator:
    print(el)
