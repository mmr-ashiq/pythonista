# we can slice list, tuple, and string

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

print(list1[0:9:2])  # start:stop:step # [1, 3, 5, 7, 9]


# if start not specified, default is 0
# if stop not specified, default is the end of the list
# if step not specified, default is 1


print(list1[:5])  # [1, 2, 3, 4, 5]
print(list1[5:])  # [6, 7, 8, 9, 10]
print(list1[::2])  # [1, 3, 5, 7, 9]
print(list1[1:5])  # [2, 3, 4, 5]
print(list1[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # copy of the list


"""
    start is included and stop is not included.
    start is 0 and stop is 9, step is 2, then we get [1, 3, 5, 7, 9]
    list[start:stop:step]: gives a list with elements list[start], list[start+step], list[start+2*step],
     list[start+3*step], ..., list[stop-1]
    step means how many elements to skip between each element.
    if we have negative steps, then start should be greater otherwise it will give empty list.
    like here, list[start + 2 * stop].
    list/tuple/string returns list/tuple/string.
"""

list2 = [49, 59, 69]
list3 = list2[:]

tuple1 = (79, 89, 99)
tuple2 = tuple1[:]

string1 = "khatam"
string2 = string1[:]

print(list2 is list3)  # False
print(tuple1 is tuple2)  # True
print(string1 is string2)  # True

# in list slicing, we always get different list as output.
# in tuple/string slicing, we always get same tuple/string as output.
# in tuple/string python return references to the same tuple/string.
