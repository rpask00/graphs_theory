import sys

n = 4
matrix = [[sys.maxsize for _ in range(n)] for __ in range(n)]

matrix = [
    [0, 2, 6, 9],
    [2, 0, 4, 4],
    [6, 4, 0, 5],
    [9, 4, 5, 0],
]


def tsp(m, sN):
    memo = [[sys.maxsize for _ in range(2**n)]for __ in range(n)]

    setup(m, memo, sN)
    solve(m, memo, sN)
    minCost = findMinCost(m, memo, sN)
    tour = findOptimalTour(m, memo, sN)

    return (minCost, tour)


def setup(m, memo, sN):
    for i in range(n):
        if i == sN:
            continue

        memo[i][1 << sN | 1 << i] = m[sN][i]

    return 0


def solve(m, memo, sN):
    for r in range(3, n+1):
        for subset in combinations(n, r):
            if notIN(sN, subset):
                continue

            for nxt in range(n):
                if nxt == sN or notIN(nxt, subset):
                    continue

                state = subset ^ (1 << nxt)
                minDist = sys.maxsize

                for endNode in range(n):
                    if endNode == sN or endNode == nxt or notIN(endNode, subset):
                        continue

                    newDist = memo[endNode][state] + m[endNode][nxt]
                    minDist = newDist if newDist < minDist else minDist

                memo[nxt][subset] = minDist


def findMinCost(m, memo, sN):
    endState =( 1 << n)-1

    mincost = sys.maxsize

    for endNode in range(n):
        if endNode == sN:
            continue

        if mincost > memo[endNode][endState]:
            mincost = memo[endNode][endState]

    return mincost


def findOptimalTour(m, memo, sN):
    state = (1 << n)-1
    path = []

    cost = sys.maxsize

    while state != 1 << sN:
        path.append(0)
        final_state = state
        for endNode in range(n):
            if notIN(endNode, state):
                continue

            if endNode == sN:
                continue

            toNextNode = m[endNode][path[-2]] if len(path) > 1 else 0

            if cost >= memo[endNode][state] + toNextNode:
                cost = memo[endNode][state] + toNextNode
                path[-1] = endNode
                final_state = state & (~(1 << endNode))

        cost = memo[path[-1]][state]
        state = final_state

    path.reverse()
    return [sN] + path


def combinations(N, r):
    maxVAl = 2**r-1 << N-r
    result = []

    def combinations_Solve(comb, r, index=0):
        if r == 0:
            result.append(comb)

        else:
            for i in range(index, n):
                comb = comb | (1 << i)

                if comb <= maxVAl:
                    combinations_Solve(comb, r-1, i+1)

                comb = comb & ~(1 << i)

    combinations_Solve(0, r, 0)
    return result


def notIN(i, subset):
    return (1 << i) & subset == 0


print(tsp(matrix, 0))
