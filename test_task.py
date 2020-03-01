def accum(s):
    returned_string = ''
    for iterator in range(0, len(s)):
        if iterator == len(s) - 1:
            returned_string += s[iterator].upper() + s[iterator].lower() * iterator
        else:
            returned_string += s[iterator].upper() + s[iterator].lower() * iterator + '-'

    return returned_string


if __name__ == '__main__':
    print(accum("ZpglnRxqenU"))