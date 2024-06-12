def create_code_with_desired_length(code, length):
    code_lst = []
    for number_of_code in range(length):
        code_lst.append(str(code)[number_of_code % len(str(code))])
    return int("".join(code_lst))


def decode(code, key):
    letter_to_number = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
        "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
    }
    number_to_letter = {value: key for key, value in letter_to_number.items()}
    int_val = create_code_with_desired_length(key, len(code))
    lst_str = list(str(int_val))
    lst_int = [int(value) for value in lst_str]
    decoded_lst = []
    for index, number in enumerate(code):
        decoded_number = number - lst_int[index]
        decoded_lst.append(number_to_letter[decoded_number])
    return "".join(decoded_lst)


if __name__ == '__main__':
    print(decode([20, 12, 18, 30, 21], 1939))
