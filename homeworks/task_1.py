"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

user_number1 = float(input("Введите Ваше первое число: "))
user_number2 = float(input("Введите Ваше второе число: "))

def user_func(a, b):
    if b == 0:
        print("К сожалению, деление на 0 невозможно, выберите другое число.")
        b = float(input("Введите Ваше новое второе число: "))
    return a / b

func = user_func
print(func(user_number1, user_number2))