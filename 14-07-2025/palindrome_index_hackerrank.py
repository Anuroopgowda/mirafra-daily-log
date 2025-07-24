def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            if s[i+1:len(s)-i] == s[i+1:len(s)-i][::-1]:
                return i
            else:
                return len(s) - 1 - i
