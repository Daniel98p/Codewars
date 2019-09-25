import collections


# def order_weight(strng):
#     print(strng.split(" "))
#     sum = 0
#     new_dict = {}
#     c = 0
#     for counter, value in enumerate(strng):
#         if value == ' ':
#             new_dict[strng[c:counter]] = sum
#             c = counter + 1
#             sum = 0
#             continue
#         sum += int(value)
#         if counter == len(strng) - 1:
#             new_dict[strng[c:counter + 1]] = sum
#     print(new_dict)
#     sorted_new_dict = sorted(new_dict.items(), key=lambda kv: kv[1])
#     print(collections.OrderedDict(sorted_new_dict))
#     returned_strng = ''
#     for counter, value in enumerate(sorted(new_dict.items(), key=lambda kv: kv[1])):
#         returned_strng += value[0]
#         if counter != len(sorted(new_dict.items(), key=lambda kv: kv[1])) - 1:
#             returned_strng += ' '
#     return (returned_strng)

def order_weight(strng):
    print(strng.split(" "))
    new_list = []
    c = 0
    sum = 0
    for counter, value in enumerate(strng):
        if value == ' ':
            new_list.append((strng[c:counter], sum))
            c = counter + 1
            sum = 0
            continue
        sum += int(value)
        if counter == len(strng) - 1:
            new_list.append((strng[c:counter + 1], sum))
    print(new_list)
    sorted_list = sorted(new_list, key=lambda x: x[1])
    print(sorted_list)
    returned_strng = ''
    for counter, value in enumerate(sorted_list):
        returned_strng += value[0]
        if counter != len(sorted_list) - 1:
            returned_strng += ' '
    return (returned_strng)



if __name__ == '__main__':
    print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))

# not good