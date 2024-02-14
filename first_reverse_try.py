def first_reverse_try(arr):
    if arr:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(first_reverse_try(lst))
