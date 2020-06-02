"""
This problem seems easily but I had to find solution to avoid runtime error on codewars server.


"""


def max_profit(prices):
    min_value = min(prices)
    profit = prices[1] - prices[0]
    if min_value != prices[-1]:
        profit = max(prices[prices.index(min_value):]) - min_value
        for number in range(prices.index(min_value) - 1):
            if max(prices[number + 1: prices.index(min_value)]) - prices[number] > profit:
                profit = max(prices[number + 1: prices.index(min_value)]) - prices[number]
    else:
        for number in range(len(prices) - 1):
            if max(prices[number + 1:]) - prices[number] > profit:
                profit = max(prices[number + 1:]) - prices[number]
    return profit


if __name__ == '__main__':
    print(max_profit([10, 7, 5, 8, 11, 9]))
