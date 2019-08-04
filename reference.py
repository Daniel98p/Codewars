def f(x):
    x = x + [2]
    return x


def g(x):
    x.append(2)
    return x


if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    print(f(my_list))
    print(my_list)
    print(g(my_list))
    print(my_list)
    print(8 in my_list)
