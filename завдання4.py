from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо рядок у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Різниця в днях
        delta_days = (birthday_this_year - today).days

        # Перевіряємо чи входить у 7 днів
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # Якщо субота або неділя — переносимо на понеділок
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.03.10"},
    {"name": "Jane Smith", "birthday": "1990.03.12"},
    {"name": "Mike Brown", "birthday": "1995.03.15"},
]

print(get_upcoming_birthdays(users))
