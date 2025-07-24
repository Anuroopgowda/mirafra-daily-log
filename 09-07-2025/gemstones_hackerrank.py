def gemstones(arr):
    common_elements = set(arr[0])
    for rock in arr[1:]:
        common_elements &= set(rock)
    return len(common_elements)
