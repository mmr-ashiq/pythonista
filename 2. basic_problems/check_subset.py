""" def is_subset(list1, list2):
    for e in list1:
        if e not in list2:
            return False
    return True """
# time complexity: O(n^2)
# space complexity: O(1)


""" def is_subset(list1, list2):
    list2 = set(list2)
    print(list2)
    for e in list1:
        if e not in list2:
            return False
    return True """
# time complexity: O(n)
# space complexity: O(n)


def is_subset(list1, list2):
    temp = dict([(e, 0) for e in list2])
    for e in list1:
        if e not in temp:
            return False
    return True
# time complexity: O(n)
# space complexity: O(n)


if __name__ == '__main__':
    list1 = [1, 3, 5, 'a', 'c']
    list2 = ['b', 'a', 3, 5, 'c', 1, 7, 7, 1, 'a']
    print(is_subset(list1, list2))
