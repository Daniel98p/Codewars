def maxSequence(arr):
    if not arr:
        return 0
    max_sum = 0
    for value in range(len(arr)):
        next_list = []
        for value1 in range(len(arr)):
            if value1 < value:
                continue
            next_list.append(arr[value1])
            if sum(next_list) > max_sum:
                max_sum = sum(next_list)
    return max_sum


if __name__ == '__main__':
    print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# it could be done better but it works




