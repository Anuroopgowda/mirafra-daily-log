def separateNumbers(s):
    for i in range(1, len(s)//2 + 1):
        first = int(s[:i])
        temp = s[:i]
        while len(temp) < len(s):
            first += 1
            temp += str(first)
        if temp == s:
            print("YES", s[:i])
            return
    print("NO")