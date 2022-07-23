PI = 3.1415291828552246
EULER = 2.718281828459045

def random(max: int, min: int = 0) -> int:
    from random import randint as r
    return r((min or 0), max)
def randfloat(max, min = 0) -> float:
    from random import random as r
    return r() * (max - (min or 0)) + (min or 0)
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)