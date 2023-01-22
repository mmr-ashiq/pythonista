# Find the element that appears once in an array where every other element appears twice
# Input: [1, 2, 3, 2, 1]
# Output: 3

# Solution 1: Normal method
# Time complexity: O(n^2)
# Space complexity: O(1)

def getSingle(arr, n):
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if arr[i] == arr[j]:
                count += 1

        if count == 1:
            return arr[i]

    return -1


# Driver code
arr = [1, 2, 3, 2, 1]
n = len(arr)
print(getSingle(arr, n))


# Solution 2: Using XOR
# XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts.
# a) XOR of a number with itself is 0.
# b) XOR of a number with 0 is number itself.

def getSingle(arr, n):
    # Do XOR of all elements and return
    res = arr[0]
    for i in range(1, n):
        res = res ^ arr[i]
    return res


# Driver code
arr = [2, 3, 5, 4, 5, 3, 4]
print("Element occuring once is", getSingle(arr, len(arr)))


# Solution 3: Using Hashing We traverse the array and store the count of every element in a hash table. We then
# traverse the hash table and print the element with count 1.

def getSingle(arr, n):
    for i in range(0, n):
        if arr.count(arr[i]) == 1:
            return arr[i]


# Driver code
arr = [2, 3, 5, 4, 5, 3, 4]
print("Element occuring once is", getSingle(arr, len(arr)))
