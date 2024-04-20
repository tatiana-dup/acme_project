from datetime import date


def birthday_count(date_of_birth: date):
    today = date.today()
    try:
        date_of_birth = date_of_birth.replace(year=today.year)
    except ValueError:
        date_of_birth = date(today.year, 3, 1)

    if date_of_birth < today:
        date_of_birth = date_of_birth.replace(year=today.year+1)

    return (date_of_birth - today).days
