def findDigits(n):
    count = 0
    for d in str(n):
        if d != '0' and n % int(d) == 0:
            count += 1
    return count
