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

que = []


def dfs(at):
    visited[at] = True
    print(at)

    for node in graph[at]:
        if visited[node]:
            continue

        visited[node] = True
        que.append(node)

    if que:
        dfs(que.pop(0))


dfs(0)
