"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_numbers = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
seasons_list = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = { seasons_list[0]: seasons_numbers[0:3],
                 seasons_list[1]: seasons_numbers[3:6],
                 seasons_list[2]: seasons_numbers[6:9],
                 seasons_list[3]: seasons_numbers[9:]
                 }

user_val = int(input("Введите число Вашего месяца: "))
for key, value in seasons_dict.items():
    if user_val in value:
        print(key)
        break
