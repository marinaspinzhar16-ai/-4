from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок у дату
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримуємо поточну дату
        today = datetime.today().date()
        
        # Обчислюємо різницю
        difference = today - given_date
        
        # Повертаємо кількість днів
        return difference.days
    
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат РРРР-ММ-ДД.")
        return None


# Приклад використання
print(get_days_from_today("2021-10-09"))
