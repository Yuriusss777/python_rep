"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def get_user_data(**qwargs):
    user_data = f'{name} {surname} {year_birth} года рождения, проживает в городе {city}, email: {e_mail}, телефон: {telephone}'
    return user_data


name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
year_birth = int(input('Введите год рождения пользователя: '))
city = input('Введите город проживания пользователя: ')
e_mail = input('Введите e-mail пользователя: ')
telephone = int(input('Введите телефон пользователя: '))

print(get_user_data(name=name, surname=surname, year_birth=year_birth, city=city, e_mail=e_mail,
                    telephone=telephone))
