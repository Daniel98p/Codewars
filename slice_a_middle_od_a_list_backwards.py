def reverse_middle(lst):
    return lst[len(lst)//2: len(lst)//2-2:-1] if len(lst) % 2 == 0 else lst[len(lst)//2+1: len(lst)//2-2:-1]


if __name__ == '__main__':
    print(reverse_middle(['a', [1, 'a'], 'd', True]))
    print(reverse_middle([1, 2, 3, 4, 5]))
