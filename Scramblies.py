def scramble(s1, s2):
    repeated_value = 0
    repeated_value1 = 0
    for iterator in s2:
        for iterator1 in s2:
            if iterator1 == iterator:
                repeated_value += 1

    for iterator2 in s1:
        for iterator3 in s1:
            if iterator2 == iterator3:
                repeated_value1 += 1
    if repeated_value > repeated_value1:
        return False

    set1 = set(s2)
    set2 = set(s1)
    if set1.issubset(set2):
        return True
    return False


if __name__ == '__main__':
    print(scramble('xrszkemrcnvfw', 'wxkxqokvrc'))
