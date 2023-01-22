# Recursive implementation of n! (n-factorial)
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(4))
