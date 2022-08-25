# def remove_duplicates(list):
#     result = []

#     for value in list:
#         if value not in result:
#             result.append(value)

#     return result
#     # O(n^2)

def remove_duplicates(l):
    result = {}

    for value in l:
        if value not in result:
            result[value] = l
    return list(result.keys())
    # O(1)

print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))