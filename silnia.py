def factorial(number):
    if number == 0:
        return 0
    else:
        strong = 1
        while number > 1:
            strong = number * strong
            number -= 1
    return strong


if __name__ == '__main__':
    answer = ''
    while answer != 'N':
        my_number = int(input('Enter a number: '))
        print(factorial(my_number))
        answer = input('Do you want to continue? [Y]/N ')


