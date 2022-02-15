def average(L):
    if not L:
        return None

    return sum(L) / len(L)


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    expected_result = 3.1 # 3.0 is the expected result
    assert expected_result == average(L), 'Test failed!'