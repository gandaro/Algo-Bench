#@tailcall
def factorial(x, acc=1):
    if (x > 1): return (factorial((x - 1), (acc * x)))
    else:       return acc
