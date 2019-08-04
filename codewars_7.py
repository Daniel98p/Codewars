def disemvowel(string):
    string1 = ''
    for iterator in string:
        if iterator == 'a' or iterator == 'e' or iterator == 'i' or iterator == 'o' or iterator == 'u':
            continue
        if iterator == 'A' or iterator == 'E' or iterator == 'I' or iterator == 'O' or iterator == 'U':
            continue
        string1 += iterator
    string = string1
    return string


if __name__ == '__main__':
    print(disemvowel('Dasdheufgksiw'))
