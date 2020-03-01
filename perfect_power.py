def isPP(n):
    counter = 2
    new_list = []
    while counter != n:
        x = n ** (1 / counter)
        y = round(n ** (1 / counter))
        if x == y:
            new_list.append(y)
            new_list.append(counter)
        if n ** (1 / counter) < 2:
            break
        counter += 1
    if not new_list:
        return None
    return new_list


if __name__ == '__main__':
    print(isPP(216))
