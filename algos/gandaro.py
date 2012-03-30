#!/usr/bin/env python3
# compatible from Python 2.6 to Python 3.2
from operator import mul
from functools import reduce

# range can only handle ranges up to sys.maxint
def iterrange(a, b):
    while a < b:
        yield a
        a += 1

def factorial(x):
    assert x > 0, 'x has to be greater than or equal to 0'
    return reduce(mul, iterrange(2, x+1), 1)


if __name__ == '__main__':
    print(factorial(6))
