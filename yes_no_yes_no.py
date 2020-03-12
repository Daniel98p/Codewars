def yes_no(arr):
    returned_list = []
    while arr:
        returned_list.append(arr.pop(0))
        if arr:
            arr.append(arr.pop(0))
    return returned_list


if __name__ == '__main__':
    print(yes_no([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
