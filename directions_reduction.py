def dirReduc(arr):
    dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for i in arr:
        if result and dict[i] == result[-1]:
            result.pop()
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    b = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(b))
