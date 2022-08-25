# def is_palindrome(s):
#     result = s[::-1]
#
#     if s == result:
#         return True
#     return False

def reverse_string(s):
    result = ''
    for c in s:
        result = c + result

    return result


def is_palindrome(s):
    reversed_str = reverse_string(s)

    if reversed_str == s:
        return True
    return False


print(is_palindrome('abc'))
