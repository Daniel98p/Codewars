def side_len(x, y):
    lst = sorted([number for number in range(1, x + y) if number + x > y and number + y > x])
    for number in lst:
        sides = sorted([x, y, number])
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            lst.remove(number)
    return lst


if __name__ == '__main__':
    print(side_len(3, 4))
