def word_point(word):
    punctation = {
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10}
    point_counter = 0
    for value in word:
        point_counter += punctation[value]
    return point_counter


if __name__ == '__main__':
    print(word_point('ABZ'))
