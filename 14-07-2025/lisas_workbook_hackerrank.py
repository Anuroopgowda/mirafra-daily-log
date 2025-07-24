def workbook(n, k, arr):
    page = 1
    special = 0
    for problems in arr:
        for i in range(1, problems + 1):
            if i == page:
                special += 1
            if i % k == 0 or i == problems:
                page += 1
    return special
