import sys

id_ = 0
n = 9
matrix = [[] for _ in range(n)]

matrix[0] = [1, 2]
matrix[1] = [2]
matrix[2] = [0, 5, 3]
matrix[3] = [4]
matrix[4] = []
matrix[5] = [6]
matrix[6] = [7]
matrix[7] = [8]
matrix[8] = [5]

ids = [0 for _ in range(n)]
lowLink = [0 for _ in range(n)]
visited = [False for _ in range(n)]

def findBridges():
    bridges = []
    for i in range(n):
        if not visited[i]:
            dfs(i, bridges)

    return bridges

def dfs(node, bridges):
    print(node)
    global id_
    lowLink[node] = id_
    ids[node] = id_
    id_ += 1

    visited[node] = True
    for nxt in matrix[node]:
        if not visited[nxt]:
            dfs(nxt, bridges)
            lowLink[node] = min(lowLink[node], lowLink[nxt])
            if lowLink[nxt] > lowLink[node]:
                bridges.append((node,nxt))
        else:
            lowLink[node] = min(lowLink[node], ids[nxt])



print(findBridges())
