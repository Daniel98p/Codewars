def queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)


if __name__ == '__main__':
    print(queue_time([2, 5, 4, 8, 9, 4], 5))

    # z githuba, spróbować za jakiś czas ponownie
