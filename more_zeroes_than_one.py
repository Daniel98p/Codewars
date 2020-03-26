def dec_to_bin_without_reverse(number):
    returned_list = []
    if number > 127:
        return None
    while number != 0:
        returned_list.append(number % 2)
        number = number // 2
    return returned_list


def drop_duplicates(s):
    returned_list = []
    for value in list(s):
        if value in returned_list:
            continue
        returned_list.append(value)
    return returned_list


def more_zeros(s):
    returned_list = []
    s = drop_duplicates(s)
    for char in s:
        if dec_to_bin_without_reverse(ord(char)).count(0) > dec_to_bin_without_reverse(ord(char)).count(1):
            returned_list.append(char)
    return returned_list


if __name__ == '__main__':
    print(dec_to_bin_without_reverse(104))
    print(more_zeros('thequickbrownfoxjumpsoverthelazydog'))

