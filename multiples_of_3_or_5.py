def solution(number):
    sum_of_numbers = 0
    for iterator in range(0, number):
        if iterator % 3 == 0 or iterator % 5 == 0:
            sum_of_numbers += iterator
    return sum_of_numbers


if __name__ == '__main__':
    print(solution(10))