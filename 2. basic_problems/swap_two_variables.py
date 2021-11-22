"""
# Before swapping:
# a = 10 b = 20
# After swapping:
# a = 20 b = 10

I/p: a = "apple", s = "Samsung"
O/p: a = "Samsung", s = "apple"
"""


# function to swap two variables using addition and subtraction method
def swap_two_variables_using_add_sub(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# fucntion to swap two variable using temp variable
def swap_two_variables_using_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b


# function to swap two variables --> Mordern Approach
def swap_two_variables(a, b):
    a, b = b, a
    return a, b


# main function
def main():
    # a = 10
    # b = 20
    a = "apple"
    b = "Samsung"
    print("Before swapping:")
    print("a =", a, "b =", b)
    a, b = swap_two_variables(a, b)
    print("After swapping:")
    print("a =", a, "b =", b)


if __name__ == "__main__":
    main()
