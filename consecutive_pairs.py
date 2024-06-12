def pairs(arr):
    if len(arr) % 2 == 1:
        arr = arr[:-1]
    counter = 0
    for number in range(len(arr)):
        if number % 2 == 1 and abs(arr[number] - arr[number - 1]) == 1:
            counter += 1
    return counter


if __name__ == '__main__':
    pairs([81, 44, 80, 26, 12, 27, -34, 37, -35])
