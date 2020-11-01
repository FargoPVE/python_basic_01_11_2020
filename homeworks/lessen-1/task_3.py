"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

user_number = int(input("Ввведите Ваше число: "))

if user_number < 10:
    user_number_2 = user_number + (user_number * 10 + user_number) + (user_number * 100 + user_number * 10 + user_number)
    print(user_number_2)
elif user_number > 10 < 100:
    user_number_3 = user_number + (user_number * 1000 + user_number) + (user_number * 100000 + user_number * 1000 + user_number)
    print(user_number_3)
elif user_number > 100 < 1000:
    user_number_4 = user_number + (user_number * 100000 + user_number) + (user_number * 100000000 + user_number * 100000 + user_number)
else:
    print("Ваше число слишком большое, введите число меньще")