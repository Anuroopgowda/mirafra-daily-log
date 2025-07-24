from math import gcd
from functools import reduce

def lcm(x, y):
    return x * y // gcd(x, y)

def getTotalX(a, b):
    l = reduce(lcm, a)
    g = reduce(gcd, b)
    count = 0
    for i in range(l, g + 1, l):
        if g % i == 0:
            count += 1
    return count
