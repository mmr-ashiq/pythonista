def is_subset(list1, list2):
    list2 = set(list2)
    print(list2)
    for e in list1:
        if e not in list2:
            return False
    return True