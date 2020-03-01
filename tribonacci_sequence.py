def tribonacci(sequence, n):
    if n > 3:
        iterator = 4
        all_sequence = []
        for i in range(0, 3):
            all_sequence.append(sequence[i])
        while iterator < n + 1:
            all_sequence.append(sum(all_sequence[iterator - 4:iterator - 1]))
            iterator += 1
        return all_sequence
    else:
        return sequence[0:n]


if __name__ == '__main__':
    print(tribonacci([1, 1, 1], 10))
