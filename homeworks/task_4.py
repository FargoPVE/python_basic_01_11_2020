"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_input = input("Введите Ваше предложение: ")
my_val = user_input.split(" ")

for i, item in enumerate(my_val):
    print(i+1, item[:10])