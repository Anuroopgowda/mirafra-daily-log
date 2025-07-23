def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    result = []
    for i in range(100):
        result.extend([i] * count[i])
    return result
