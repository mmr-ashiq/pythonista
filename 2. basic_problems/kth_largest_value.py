def kth_largest(arr, k):
    arr.sort()
    return arr[-k]


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print(kth_largest(arr, k))