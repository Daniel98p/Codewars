def dig_pow(n, p):
    result = 0
    for value in str(n):
        result += int(value) ** p
        p += 1
    if result % n == 0:
        return result / n
    return -1


if __name__ == '__main__':
    print(dig_pow(46288, 3))

