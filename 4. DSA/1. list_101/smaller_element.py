# function that take list and a value and return elements which are smaller than the value


def get_smallest_value(list1, value):
    smaller_list = []
    for i in list1:
        if i < value:
            smaller_list.append(i)
    return smaller_list


def get_smaller(list, value):
    if list is None or len(list) == 0:
        return None
    else:
        return [x for x in list if x < value]


if __name__ == '__main__':
    list1 = []
    print(get_smaller(list1, 5))

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_smallest_value(list1, 6))
