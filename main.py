lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
lst_new = []
for el in lst:
    if lst.count(el) > 1:
        continue
    lst_new.append(el)
        # print(el)
#     if lst[i] in range(i + 1, len(lst)):
#         continue
#     lst_new.append(lst[i])

print(lst_new)
