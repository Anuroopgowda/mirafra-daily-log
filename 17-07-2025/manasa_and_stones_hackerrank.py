def stones(n, a, b):
    result = set()
    for i in range(n):
        result.add(i * b + (n - 1 - i) * a)
    return sorted(result)
