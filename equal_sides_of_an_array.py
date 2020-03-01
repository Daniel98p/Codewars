def find_even_index(arr):
    first_sum = 0
    second_sum = 0
    for iterator in arr:
        first_sum += iterator
    for iterator1 in range(0, len(arr)):
        if second_sum == (first_sum - arr[iterator1]) / 2:
            return iterator1
        second_sum += arr[iterator1]
        print(second_sum)
    return -1


if __name__ == '__main__':
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]))

