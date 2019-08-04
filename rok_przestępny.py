def is_leap(year):
   return (year % 4 == 0 and year % 100 !=0) or year % 400 == 0


def leap_years(n):
    year = 2019
    while n > 0:
        if is_leap(year):
            print(f'{year} ')
            n -= 1
        year += 1


if __name__ == '__main__':
    my_n = int(input("Enter the number of years: "))
    leap_years(my_n)

