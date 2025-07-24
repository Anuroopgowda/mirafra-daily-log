from collections import deque

def bfs(graph):
    queue=deque()
    result=[]
    queue.append(0)
    while queue:
        n=queue.popleft()
        result.append(n)
        for node in graph[n]:
            if node not in result:
                queue.append(node)
    return result



def dfs(graph, start):
    visited = set()
    result = []

    def dfs_helper(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return result



graph_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}
print("bfs:",bfs(graph_list))
print("dfs:",dfs(graph_list))

