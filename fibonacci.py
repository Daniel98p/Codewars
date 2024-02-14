def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    if n == 0 or n == 1:
        return n
    first_value = 0
    second_value = 1
    result = 1
    for _ in range(n - 1):
        result = first_value + second_value
        first_value = second_value
        second_value = result

    return result


if __name__ == "__main__":
    print(fibonacci(5))