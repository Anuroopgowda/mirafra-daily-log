def superDigit(n, k):
    def digit_sum(x):
        if len(x) == 1:
            return int(x)
        return digit_sum(str(sum(int(d) for d in x)))

    initial_sum = str(sum(int(d) for d in n) * k)
    return digit_sum(initial_sum)
