"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

user_revenue = int(input("Введите значение выручки: "))
user_cost = int(input("Введите значение издержки: "))

if user_revenue > user_cost:
    print("Ваша фирма работает работает с прибылью")
    user_proceeds = user_revenue - user_cost
    user_profitability = user_revenue // user_proceeds
    print("Рентабельность Вашей фирмы равна: ")
elif user_revenue < user_cost:
    print("Ваша фирма работает с убытками")
elif user_revenue == user_cost:
    print("Ваша фирма работает в ноль (прибыль равна издержкам)")
else:
    print("Ваши значения не соответствуют условиям программы")

user_staff = int(input("Введите численность сотрудников Вашей фирмы: "))
user_profit = user_revenue / user_staff
print("Прибыль на одного сотрудника равна: ", user_profit)

