def sumXor(n):
    if n == 0:
        return 1
    zero_bits = bin(n).count('0') - 1
    return 2 ** zero_bits
