def largestPermutation(k, arr):
    n = len(arr)
    pos = {val: idx for idx, val in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        expected = n - i
        if arr[i] != expected:
            to_swap_idx = pos[expected]
            arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
            pos[arr[to_swap_idx]] = to_swap_idx
            pos[arr[i]] = i
            k -= 1
    return arr
