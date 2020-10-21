matrix = [
    [1],
    [2],
    [0],
    [4, 7],
    [5],
    [0, 6],
    [0, 2, 4],
    [3, 5],
]
n = len(matrix)
visited = [False for i in range(n)]
stack = []
lowLink = [0 for _ in range(n)]
ids = [0 for _ in range(n)]
id_ = 0
SCCs = []

ids = [7, 5, 4, 6, 3, 1, 2, 0]


def Tarjans():
    for node in range(n):
        if not visited[ids[node]]:
            dfs(ids[node])

    return SCCs


def dfs(node):
    visited[node] = True

    # print(node)

    global id_
    stack.append(node)

    lowLink[node] = initialValue = id_
    id_ += 1

    for nxt in matrix[node]:
        if not visited[nxt]:
            dfs(nxt)

        if nxt not in stack:
            continue

        lowLink[node] = min(lowLink[node], lowLink[nxt])

        if lowLink[node] == initialValue:
            scc = [stack.pop()]
            while scc[-1] != node:
                scc.append(stack.pop())

            SCCs.append(list(reversed(scc)))


print(Tarjans())
