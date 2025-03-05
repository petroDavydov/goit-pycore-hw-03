from datetime import datetime


def get_days_from_today(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date_time_today = datetime.today()
        result = (date_time_today - date_obj).days
        return f"Number of days between a given date and the current date: {result}"
    except ValueError:
        return ("Please enter day in format as 'YYYY-mm-dd'. Thank You !")


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-10-09"))
