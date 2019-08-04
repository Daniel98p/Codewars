def sort(lst):
    next_list = lst
    index = lst[len(lst)-1]
    for value in lst:
        for second_walue in
            if value < index:
                bufor = value
                value = index
                index = bufor
            index -= 1
    return lst




def min_list(lst):
    index = 0
    minimum = lst[0]
    while index < len(lst):
        if lst[index] < minimum:
            minimum = lst[index]
        index += 1
    return minimum


def get_index(processed_list, value):
    index = 0
    list1 = []
    while index < len(processed_list):
        if processed_list[index] == value:
            list1.append(index)
        index += 1
    return list1


def get_in(processed_list, value):
    for val in processed_list:
        if val == value:
            return True
    return False


if __name__ == '__main__':
    my_list = [1, 3, 6, 4, 7, 2, 7, 9]
    # print(min_list(my_list))
    #print(get_index(my_list, 7))
    # print(get_in(my_list, 7))
    print(sort(my_list))

