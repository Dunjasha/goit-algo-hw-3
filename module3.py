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

def get_numbers_ticket(min, max, quantity):
    # Функція повертає відсортований список унікальних випадкових чисел у заданому діапазоні.
    
    if not (1 <= min <= max <= 1000) or quantity > (max - min + 1):
        return []  # Повертаємо пустий список у разі некоректних даних
    
    return sorted(random.sample(range(min, max + 1), quantity))  # Генеруємо, сортуємо та повертаємо список

if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6)) 

