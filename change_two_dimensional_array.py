def matrix(array):
    for index, sub_array in enumerate(array):
        sub_array[index] = 0 if sub_array[index] < 0 else 1
    return array


if __name__ == '__main__':
    print(matrix([[1, 2, 3], [4, 5, 6], [-3, -4, -6]]))

