def count_smileys(arr):
    smileys_counter = 0
    for iterator in arr:
        if len(iterator) == 3:
            if iterator[0] == ':' or iterator[0] == ';' and iterator[1] == '-' or iterator[1] == '~' and iterator[2] == ')' or iterator[2] == 'D':
                smileys_counter += 1
        if len(iterator) == 2:
            if iterator[0] == ':' or iterator[0] == ';' and iterator[1] == ')' or iterator[1] == 'D':
                smileys_counter += 1
    return smileys_counter


if __name__ == '__main__':
    print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
