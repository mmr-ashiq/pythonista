def getEvenOdd(list):
    even = []
    odd = []
    for x in list:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    return even, odd


list = [1, 2, 3, 4, 5, 6, 7, 8]

print(getEvenOdd(list))
