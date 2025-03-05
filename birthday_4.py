from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    birthday_list_date = []  # list with birthday
    today_data_day = datetime.today().date()  # today date

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue
        birthday_this_year = birthday.replace(year=today_data_day.year)

        if birthday_this_year < today_data_day:
            birthday_this_year = birthday_this_year.replace(
                year=today_data_day.year + 1)

        days_until_birthday = (birthday_this_year - today_data_day).days

        if 0 <= days_until_birthday < 7:
            congrat_day = today_data_day + timedelta(days=days_until_birthday)

            if birthday_this_year.weekday() >= 5:
                next_work_day = today_data_day + \
                    timedelta(days=(7 - today_data_day.weekday()))
                congrat_day = next_work_day

            birthday_list_date.append(
                {"name": user["name"], "congrat_day": congrat_day.strftime("%Y.%m.%d"), })

    return birthday_list_date


users = [
    {"name": "John Doe", "birthday": "1985.03.10"},
    {"name": "Jane Smith", "birthday": "1990.03.8"},
    {"name": "Invalid User", "birthday": "invalid_date"},
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
