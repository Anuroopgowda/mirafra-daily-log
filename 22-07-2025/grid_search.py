def gridSearch(G, P):
    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            match = True
            for k in range(r):
                if G[i + k][j:j + c] != P[k]:
                    match = False
                    break
            if match:
                return "YES"
    return "NO"
