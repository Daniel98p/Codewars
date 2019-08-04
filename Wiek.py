def century(year):
    if year > 0:
        if year % 100 > 0:
            return year // 100 + 1
        else:
            return year // 100
    if year < 0:
        return year // 100


if __name__ == '__main__':
    my_year = -10000
    print(century(my_year))


