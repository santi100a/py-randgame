def random(max, min = 0) -> int:
    from random import randint as __ri
    return __ri((min or 0), max)
def randfloat(max, min = 0) -> float:
    from random import random as __r
    return __r() * (max - (min or 0)) + (min or 0)
def randspread(max: float, min: float = 0.0) -> float:
    from random import random as __r
    return __r() * (max - (min or 0)) + (min or 0)
PI = 3.1415291828552246
EULER = 2.718281828459045