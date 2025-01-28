# Перше завдання
from datetime import datetime

def get_days_from_today(date):
        try:
            input_date = datetime.strptime(date, '%Y-%m-%d').date()
            now = datetime.today().date()
            difference = (now - input_date).days
            return difference
        except ValueError:
              print("Не правельні введеня даних")
        

print(get_days_from_today('2020-10-09'))

# Друге завдання
import random

def get_numbers_ticket(min, max, quantity): # Функція для видачі випадкових білетів
    your_bilet = [] # Робимо квиток для людини.
    if not 1 > min and not 1000 < max: # Превірає аргументи.
        your_name = input("Введить своє ім'я: ") # Дізнаємося ім'я людини.
        for i in range(quantity): # Робить випадкові числа для your_bilet
            bilet_loter = random.randint(min, max) # Робить випадкові білети.
            your_bilet.append(bilet_loter) # Дамо білет для людини.
        print(f"Твій білет {your_bilet}, {your_name}") # Виведіть ваш квиток.
    else:
        print(f"Ви вели не правільні числа {min} чи {max}.") # Виводить неправильні числа, які ввели.

if __name__ == "__main__":
    get_numbers_ticket(1, 49, 6)


# number_for_winer = [15, 46, 14, 6, 26, 37]
# if set(number_for_winer) == set(bilet):
#         print(f"Winner bilet1")
# else:
#     print(f"Winner bilet2")