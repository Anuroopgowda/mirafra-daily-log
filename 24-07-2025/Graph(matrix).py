from collections import deque

class GraphMatrix:
    def __init__(self, vertices):
        self.size = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in range(self.size):
                    if self.matrix[node][neighbor] == 1:
                        queue.append(neighbor)
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_helper(v):
            visited.add(v)
            result.append(v)
            for neighbor in range(self.size):
                if self.matrix[v][neighbor] == 1 and neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result
