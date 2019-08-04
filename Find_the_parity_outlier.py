def find_outlier(integers):
    odd_values = []
    even_values = []
    for value in integers:
        if value % 2:
            odd_values.append(value)
        elif value % 2 == 0:
            even_values.append(value)
    if len(odd_values) == 1:
        s = [str(i) for i in odd_values]
        res = int("".join(s))
        return res
    elif len(even_values) == 1:
        s = [str(i) for i in even_values]
        res = int("".join(s))
        return res
    return None


if __name__ == '__main__':
    print(find_outlier([2, 3, 4, 6, 8]))



