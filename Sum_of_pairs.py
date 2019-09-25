def sum_pairs(ints, s):
    for value in range(0, len(ints)):
        for value1 in range(0, len(ints)):
            if value1 > value:
                if ints[value] + ints[value1] == s:
                    for value2 in range(0, value1):
                        for value3 in range(0, value1):
                            if value3 > value2:
                                if ints[value2] + ints[value3] == s:
                                    return [ints[value2], ints[value3]]
                    return [ints[value], ints[value1]]
    return None


if __name__ == '__main__':
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

