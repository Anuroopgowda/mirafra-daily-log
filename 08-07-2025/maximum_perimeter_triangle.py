def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks)-3, -1, -1):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return sticks[i:i+3]
    return [-1]