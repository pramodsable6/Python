def factorial(n):
    """
    n: Integer to determine factorial of
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
