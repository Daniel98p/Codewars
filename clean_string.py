def clean_string(s):
    help_list = []
    returned_string = ""
    for value in s:
        if value == '#':
            if len(help_list) == 0:
                continue
            else:
                help_list.pop()
        else:
            help_list.append(value)
    for value in help_list:
        returned_string += value
    return returned_string


if __name__ == '__main__':
    print(clean_string("abc#d##c"))
