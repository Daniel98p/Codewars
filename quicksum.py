import string


def quicksum(packet):
    result = 0
    alphabet = string.ascii_uppercase
    letter_number_map = {}
    for letter_index in range(len(alphabet)):
        letter_number_map.update({alphabet[letter_index]: letter_index + 1})
    for index, char in enumerate(packet):
        if char in alphabet:
            result += (index + 1) * letter_number_map[char]
        elif char == " ":
            result += 0
        else:
            result = 0
            break
    return result


if __name__ == '__main__':
    print(quicksum("234 234 WEF ASDF AAA 554211 ???? "))
