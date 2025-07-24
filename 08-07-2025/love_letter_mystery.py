# The Love-Letter Mystery

def theLoveLetterMystery(s):
    count = 0
    n = len(s)
    for i in range(n // 2):
        count += abs(ord(s[i]) - ord(s[n - i - 1]))
    return count

# Sample Input
t = 1
strings = ["abc"]

# Sample Output
for s in strings:
    print(theLoveLetterMystery(s))
