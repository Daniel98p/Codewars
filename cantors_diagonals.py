def cantor(nested_list):
    return [1 if lst[index] == 0 else 0 for index, lst in enumerate(nested_list)]
