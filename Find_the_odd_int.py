def find_it(seq):
    odd_number_counter = 0
    for iterator in seq:
        for iterator1 in seq:
            if iterator1 == iterator:
                odd_number_counter += 1
        if odd_number_counter % 2:
            return iterator
        else:
            odd_number_counter = 0
    return None


if __name__ == '__main__':
    print(find_it([2, 2, 3, 3, 4, 4, 5, 5]))

