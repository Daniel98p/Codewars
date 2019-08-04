def digital_root(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while len(str(n)) != 1:
            addition = 0
            for iterator in str(n):
                addition += int(iterator)
            n = addition
        return addition


if __name__ == '__main__':
    print(digital_root(456))
