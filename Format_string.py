def format_string(s):
    new_string = ' '
    for value in s:
        if not value in new_string:
            new_string += value
            new_string += str(s.count(value))
    return new_string


if __name__ == '__main__':
    print(format_string(' AAAAaaBCCCDDe'))
