"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""

my_list = [15, 40, 50, 120, 66, 91, 73, 502, 400]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)