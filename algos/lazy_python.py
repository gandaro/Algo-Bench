def factorial(x):
    return x > 1 and x * factorial(x - 1) or 1
