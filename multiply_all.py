def multiply_all(arr):
    def second_func(value):
        return [number * value for number in arr]

    return second_func
