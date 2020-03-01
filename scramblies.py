def scramble(s1, s2):
    for value in s2:
        if s1.count(value) < s2.count(value):
            return False
    set1 = set(s2)
    set2 = set(s1)
    if set1.issubset(set2):
        return True
    return False


if __name__ == '__main__':
    print(scramble('xrszkemrcnvfw', 'wxkxqokvrc'))
