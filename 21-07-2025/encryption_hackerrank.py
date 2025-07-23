import math

def encryption(s):
    s = s.replace(" ", "")
    rows = math.floor(math.sqrt(len(s)))
    cols = math.ceil(math.sqrt(len(s)))
    if rows * cols < len(s):
        rows += 1

    result = []
    for c in range(cols):
        result.append(''.join(s[r * cols + c] for r in range(rows) if r * cols + c < len(s)))

    return ' '.join(result)
