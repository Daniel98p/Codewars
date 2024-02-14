def get_max_under_value(lst, maxi):
    for value in sorted(lst, reverse=True):
        if value <= maxi:
            return value


def latest_clock(a, b, c, d):
    numbers = [a, b, c, d]
    first_number = get_max_under_value(numbers, 2)
    numbers.pop(numbers.index(first_number))
    second_number = get_max_under_value(numbers, 9) if first_number == 1 else str(get_max_under_value(numbers, 3))
    numbers.pop(numbers.index(second_number))
    third_number = get_max_under_value(numbers, 5)
    numbers.pop(numbers.index(third_number))
    fourth_number = get_max_under_value(numbers, 9)
    return str(first_number) + str(second_number) + ":" + str(third_number) + str(fourth_number)


if __name__ == "__main__":
    print(latest_clock(1, 9, 8, 3))