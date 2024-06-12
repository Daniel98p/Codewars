def delete_but_first_and_last(list_to_process):
    del list_to_process[1:len(list_to_process) - 1]
    print(list_to_process)


def delete_but_first_and_last_2(list_to_process):
    index = 0
    length = len(list_to_process)
    while index < length:
        if 0 < index < length - 1:
            list_to_process.pop(1)
        index += 1
    return list_to_process


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6]
    # delete_but_first_and_last(my_list)
    print(delete_but_first_and_last_2(my_list))
