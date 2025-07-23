def organizingContainers(container):
    row_sums = [sum(row) for row in container]
    col_sums = [sum(container[i][j] for i in range(len(container))) for j in range(len(container))]
    return "Possible" if sorted(row_sums) == sorted(col_sums) else "Impossible"
