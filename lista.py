if __name__ == '__main__':
    lst = [1, 4, 5, 8, 4, 0, 3]
    print(lst[4:7])

    lst2 = [2, 6.7, 'aaaa']
    print(lst2[0:3])
    lst2.append('bbb')
    print(lst2[0:4])
    lst2[1] = 'replaced text'
    print(lst2)
    print(lst2[0:4:2])
    lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lst3[::-1])
