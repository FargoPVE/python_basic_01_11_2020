"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    return max(a+b, b+c, a+c)

my_list = []
for x in range(3):
    number = int(input("Введите Ваше число: "))
    my_list.append(number)

print(my_func(my_list[0], my_list[1], my_list[2]))