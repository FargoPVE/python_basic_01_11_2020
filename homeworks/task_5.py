"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_rating = [10, 8, 8, 6, 4, 1]

user_input = int(input("Введите Ваше число рейтинга: "))

val_for_rating = my_rating.count(user_input)

if val_for_rating == 0:
    if user_input > my_rating[0]:
        my_rating.insert(0, user_input)
    elif user_input < my_rating[-1]:
        my_rating.append(user_input)
    else:
        for x in my_rating:
            f = my_rating.index(user_input - 1)
            my_rating.insert(f, user_input)
            break
else:
    my_new_rating = my_rating.count(user_input) + my_rating.index(user_input)
    my_rating.insert(my_new_rating, user_input)

print(my_rating)
