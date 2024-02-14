def is_leap_year(year):
    if not year % 4:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False
