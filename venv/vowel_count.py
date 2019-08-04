def getCount(inputStr):
    num_vowels = 0
    for iterator in inputStr:
        if iterator == 'a' or iterator == 'e' or iterator == 'i' or iterator == 'o' or iterator == 'u':
            num_vowels += 1

    return num_vowels

if __name__ == '__main__':
    print(getCount('abcde'))