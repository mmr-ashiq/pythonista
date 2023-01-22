""" 
i/p: [10, 20, 30]
o/p: yes
"""


def isListSorted(a):
    if a is None or len(a) == 0:
        return True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


if __name__ == '__main__':
    list1 = []
    print(isListSorted(list1))

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(isListSorted(list1))

    list1 = [50, 20, 10]
    print(isListSorted(list1))
