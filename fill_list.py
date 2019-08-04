def fill(number):
    lst = []
    index = 0
    while index < number:
        lst.append(number)
        index += 1
        number *= 1 / 2

    return lst


if __name__ == '__main__':
    print(fill(100))
    my_lst = fill(100)
    my_lst.pop()
    my_lst.pop()
    my_lst.pop()
    my_lst.pop()
    print(my_lst)
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lst1[2:8])
    print(lst1[::2])


