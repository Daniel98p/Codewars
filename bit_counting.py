def count_bits(n):
    binary_numbers = []
    while n > 0:
        binary_numbers.append(n % 2)
        n //= 2
    return binary_numbers.count(1)


if __name__ == '__main__':
    print(count_bits(9))

