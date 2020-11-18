"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""
from itertools import count, cycle

def my_func(x,y):
    for el in count(x):
        if el > y:
            break
        else:
            print(el)
    return my_func


first_input = int(input("Введите число-начало генератора: "))
second_input = int(input("Введите число-конец генератора: "))
print(my_func(first_input, second_input))

my_list = [el for el in range(1, 8, 2)]

i = 0
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1