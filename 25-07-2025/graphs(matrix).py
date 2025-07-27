def bfs(graph):
    stack = []
    visited = []
    stack.append(0)
    while stack:
        vertice = stack.pop(0)
        if vertice not in visited:
            visited.append(vertice)
        else:
            continue
        for i in range(len(graph[vertice])):
            if graph[vertice][i] == 1:
                stack.append(i)
    return visited


def dfs(graph):
    stack = []
    visited = []
    stack.append(0)
    while stack:
        vertice = stack.pop()
        if vertice not in visited:
            visited.append(vertice)
        else:
            continue
        for i in range(len(graph[vertice]) - 1, -1, -1):
            if graph[vertice][i] == 1:
                stack.append(i)
    return visited


def prims(graph):
    selected = []
    priority = []
    weight = 0
    priority.append([0, 0])
    while priority:
        lst = priority.pop(0)
        node = lst[0]
        if node not in selected:
            weight += lst[1]
            selected.append(node)
        else:
            continue
        for i in range(len(graph[node])):
            if i not in selected and graph[node][i] > 0:
                priority.append([i, graph[node][i]])
        print(priority)
        if len(priority) == 0:
            break
        priority = sorted(priority, key=lambda x: x[1])
    return selected, weight


adj_matrix = [
    [0, 1, 1, 0, 0],  # 0 -> 1, 2
    [1, 0, 0, 1, 0],  # 1 -> 0, 3
    [1, 0, 0, 0, 1],  # 2 -> 0, 4
    [0, 1, 0, 0, 0],  # 3 -> 1
    [0, 0, 1, 0, 0]  # 4 -> 2
]

adj_matrix2 = [
    [0, 1, 0, 1, 0],  # 0 -> 1, 3
    [1, 0, 1, 0, 0],  # 1 -> 0, 2
    [0, 1, 0, 1, 1],  # 2 -> 1, 3, 4
    [1, 0, 1, 0, 0],  # 3 -> 0, 2
    [0, 0, 1, 0, 0]  # 4 -> 2
]

graph = [
    [0, 1, 3, 4],  # A
    [1, 0, 2, 5],  # B
    [3, 2, 0, 0],  # C
    [4, 5, 0, 0]  # D
]

test_matrix = [
    [0, 2, 6, 0, 0],  # 0 connected to 1 (2), 2 (6)
    [2, 0, 4, 7, 0],  # 1 connected to 0, 2 (4), 3 (7)
    [6, 4, 0, 5, 0],  # 2 connected to 0, 1, 3 (5)
    [0, 7, 5, 0, 9],  # 3 connected to 1, 2, 4 (9)
    [0, 0, 0, 9, 0]  # 4 connected to 3
]

# print(bfs(adj_matrix2))
# print(dfs(adj_matrix2))
# print(prims(graph))
print(prims(test_matrix))

lst = [[1, 2], [3, 4], [2, 1]]


def dfs(matrix, start):
    visited = []
    stack = [start]

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            print(curr, end=' ')
            # Push neighbors in reverse order (high to low)
            for neighbor in reversed(range(len(matrix[curr]))):
                if matrix[curr][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
    return visited

def bfs(matrix, start):
    visited = []
    stack = [start]

    while stack:
        curr = stack.pop(0)
        if curr not in visited:
            visited.append(curr)
            # print(curr, end=' ')
            # Push neighbors in reverse order (high to low)
            for neighbor in range(len(matrix[curr])):
                if matrix[curr][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
    return visited


# Adjacency matrix
adj_matrix = [
    [0, 1, 1, 0, 0],  # 0 -> 1, 2
    [1, 0, 0, 1, 0],  # 1 -> 0, 3
    [1, 0, 0, 0, 1],  # 2 -> 0, 4
    [0, 1, 0, 0, 0],  # 3 -> 1
    [0, 0, 1, 0, 0]   # 4 -> 2
]

print(bfs(adj_matrix,0))
print(dfs(adj_matrix, 0))



# Prim's Algorithm in Python


INF = 9999999
# number of vertices in graph
V = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1


# Kruskal's algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()