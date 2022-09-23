""" def count_characters(s):
    result = {}

    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
            
    for key, value in result.items():
        print(key, value)

"""

""" from collections import defaultdict

def count_characters(s):
    result = defaultdict(int)

    for c in s:
        result[c] += 1

    for key, value in result.items():
        print(key, value) """


def count_characters(s):
    result = {}

    for c in s:
        result[c] = result.get(c, 0) + 1

    for key, value in result.items():
        print(key, value)


if __name__ == '__main__':
    s = input()
    count_characters(s)
