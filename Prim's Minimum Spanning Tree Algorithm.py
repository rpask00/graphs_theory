import heapq
import sys
hq = []
heapq.heapify(hq)


n = 8
matrix = [[sys.maxsize for _ in range(n)] for __ in range(n)]

matrix[0][1] = 10
matrix[0][2] = 1
matrix[0][3] = 4
matrix[1][0] = 10
matrix[2][2] = 3
matrix[1][4] = 0
matrix[2][0] = 1
matrix[2][1] = 3
matrix[2][3] = 2
matrix[2][5] = 8
matrix[3][0] = 4
matrix[3][2] = 2
matrix[3][5] = 2
matrix[3][6] = 7
matrix[4][1] = 0
matrix[4][5] = 1
matrix[4][7] = 8
matrix[5][2] = 8
matrix[5][3] = 2
matrix[5][4] = 1
matrix[5][6] = 6
matrix[5][7] = 9
matrix[6][3] = 7
matrix[6][5] = 6
matrix[6][7] = 12
matrix[7][4] = 8
matrix[7][5] = 9
matrix[7][6] = 12

visited = [False for i in range(n)]
spanningTree = []
cost = 0

def prim(node):
    global cost
    visited[node] = True
    if all(visited):
        return

    for nxt, weight in enumerate(matrix[node]):
        if weight == sys.maxsize:
            continue

        if visited[nxt]:
            continue

        heapq.heappush(hq, (weight, node, nxt))

    weight, node, nxt = heapq.heappop(hq)

    while visited[nxt]:
        weight, node, nxt = heapq.heappop(hq)

    spanningTree.append((node, nxt))
    cost += weight
    prim(nxt)


prim(0)

print(spanningTree)
print(cost)
