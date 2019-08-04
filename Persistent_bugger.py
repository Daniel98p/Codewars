def persistence(n):
    returned_sum = 0
    while len(str(n)) != 1:
        variable = 1
        for iterator in str(n):
            variable *= int(iterator)
        n = variable
        returned_sum += 1
    return returned_sum


if __name__ == '__main__':
    print(persistence(39))

