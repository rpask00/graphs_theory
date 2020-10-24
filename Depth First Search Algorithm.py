graph = [
    [2, 4, 6],
    [2, 3],
    [0, 1, 4, 6],
    [1, 5],
    [0],
    [3],
    [0, 2]
]
n = len(graph)

visited = [False for i in range(n)]

def dfs(at):
    if visited[at]:
        return True

    print(at)
    visited[at] = True

    for node in graph[at]:
        dfs(node)


dfs(0)
