#@tailcall
def factorial(x, acc=1):
    if x: return factorial(x.__sub__(1), acc.__mul__(x))
    return acc
