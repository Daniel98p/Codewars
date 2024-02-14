from re import Match, search


def alphanumeric(password):
    if len(password) == 0:
        return False
    for character in password:
        if type(search("[0-9]", character)) == Match or type(search("[a-zA-Z]", character)) == Match:
            continue
        return False
    return True


if __name__ == '__main__':
    print(alphanumeric("PassW0rd"))
