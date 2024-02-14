import statistics


def mean(lst):
    int_values = []
    text = ""
    for value in lst:
        try:
            val = int(value)
            int_values.append(val)
        except ValueError:
            text += value
    return [statistics.mean(int_values), text]


if __name__ == '__main__':
    l = ["u", "6", "d", "1", "i", "w", "6", "s", "t", "4", "a", "6", "g", "1", "2", "w", "8", "o", "2", "0"]
    print(mean(l))
