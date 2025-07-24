def misereNim(s):
    from functools import reduce
    xor_sum = reduce(lambda x, y: x ^ y, s)
    if all(x == 1 for x in s):
        return "Second" if len(s) % 2 == 0 else "First"
    return "First" if xor_sum != 0 else "Second"
