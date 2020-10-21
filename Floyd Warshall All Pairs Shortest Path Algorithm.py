import sys

n = 10
dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
matrix = [[sys.maxsize for _ in range(n)] for _ in range(n)]
nxt = [[sys.maxsize for _ in range(n)] for _ in range(n)]

matrix[0][1] = 5
matrix[1][2] = 20
matrix[1][5] = 30
matrix[1][6] = 60
matrix[2][3] = 10
matrix[2][4] = 75
matrix[3][2] = -15
matrix[4][9] = 100
matrix[5][4] = 25
matrix[5][6] = 5
matrix[5][8] = 50
matrix[6][7] = -50
matrix[7][8] = -10


def setup():
    for i in range(n):
        dp[i][i] = 0
        for j in range(n):
            dp[i][j] = matrix[i][j]

            if dp[i][j] != sys.maxsize:
                nxt[i][j] = j


def floydWarshall():
    setup()

    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or j == i:
                    continue

                if dp[i][k] + dp[k][j] < dp[i][j]:

                    dp[i][j] = dp[i][k] + dp[k][j]
                    nxt[i][j] = nxt[i][k]

    handle_negative_cycle()
    return dp


def handle_negative_cycle():
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or j == i:
                    continue

                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = -sys.maxsize


def get_path(from_, to_):
    path = []

    curr = from_

    while curr != to_:
        if curr == sys.maxsize:
            return []

        path.append(curr)
        curr = nxt[curr][to_]

    path.append(to_)
    return path


for i, row in enumerate(floydWarshall()):
    print(i, [r for r in row])


print(get_path(1, 8))
