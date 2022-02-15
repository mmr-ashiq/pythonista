def average(L):
    if not L:
        return None

    return sum(L) / len(L)


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    expected_result = 3.0
    program_output = average(L)

    if expected_result == program_output:
        print('Test passed')
    else:
        print('Test failed!', 'Expected:', expected_result, 'Got:', program_output)
