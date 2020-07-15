def thirt(n):
    values = [1, 10, 9, 12, 3, 4]
    tmp_result = n
    while True:
        result = 0
        values_counter = 0
        tmp_result = [int(x) for x in str(tmp_result)]
        for number in range(len(tmp_result)-1, -1, -1):
            if values_counter > 5:
                values_counter = 0
            result += values[values_counter] * tmp_result[number]
            values_counter += 1
        tmp = [str(x) for x in tmp_result]
        tmp_result = "".join(tmp)
        int(tmp_result)
        if result == int(tmp_result):
            break
        else:
            tmp_result = result
    return result


if __name__ == '__main__':
    print(thirt(1234567))





