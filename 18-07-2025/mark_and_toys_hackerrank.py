def maximumToys(prices, k):
    prices.sort()
    count = 0
    total = 0
    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break
    return count
