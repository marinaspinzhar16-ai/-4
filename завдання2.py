import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності параметрів
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1) or quantity <= 0:
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортування результату
    numbers.sort()

    return numbers


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
