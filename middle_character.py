def get_middle(s):
    string = []
    for iterator in s:
        string.append(iterator)
    if len(string) % 2:
        return string[len(string)//2]
    else:
        return string[len(string)//2 - 1] + string[len(string)//2]


if __name__ == '__main__':
    print(get_middle('wwrwpp'))

