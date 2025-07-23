def flippingMatrix(matrix):
    n = len(matrix) // 2
    total = 0
    for i in range(n):
        for j in range(n):
            total += max(
                matrix[i][j],
                matrix[i][2 * n - j - 1],
                matrix[2 * n - i - 1][j],
                matrix[2 * n - i - 1][2 * n - j - 1]
            )
    return total
