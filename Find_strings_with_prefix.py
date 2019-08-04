def find_strings(lst, prefix):
    lst_of_new_strings = []
    for value in lst:
        if value[0:len(prefix)] == prefix:
            lst_of_new_strings.append(value)
    return lst_of_new_strings


if __name__ == '__main__':
    print(find_strings(['wyhn', 'we', 'wyj', 'ik'], 'wy'))


