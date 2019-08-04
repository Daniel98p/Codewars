def adding_list(lst1, lst2):
    return lst1 + lst2


def extend_list(lst1, lst2):
      lst1.extend(lst2)
      print(lst1)


def clip_text(lst1, lst2):
    index = 0
    lst1.extend(lst2)
    while index < len(lst1):
        text = lst1[index]
        text = text[:3]
        lst1[index] = text
        index += 1
    return lst1


if __name__ == '__main__':
    my_list1 = ['aaaa', 'bbbb', 'cccc']
    my_list2 = ['dddd', 'eeee', 'ffff']
    print(adding_list(my_list1, my_list2))
    extend_list(my_list1, my_list2)
    print(clip_text(my_list1, my_list2))


