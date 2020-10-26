
import sys


class Graph:
    verticies = {}
    nodesCount = 0
    edges = []

    class Vertex:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.visitedToken = 0

    class Edge:
        residual = None

        def __init__(self, from_, to_, isResidual, maxCapacity):
            self.from_ = from_
            self.to_ = to_
            self.isResidual = isResidual
            self.capacity = maxCapacity
            self.flow = 0

        def augment(self, bootleneck):
            self.flow += bootleneck
            self.residual.flow -= bootleneck

        def remainingCapacity(self):
            return self.capacity - self.flow

    def addEdge(self, from_, to_, capacity):
        key = f'{from_},{to_}'
        if key in self.edges:
            return

        if from_ not in self.verticies:
            self.addVertex(from_)

        if to_ not in self.verticies:
            self.addVertex(to_)

        from_ = self.verticies[from_]
        to_ = self.verticies[to_]

        main = self.Edge(from_, to_, False, capacity)
        residual = self.Edge(to_, from_, True, 0)

        main.residual = residual
        residual.residual = main

        from_.edges.append(main)
        to_.edges.append(residual)

        self.edges.append(key)

    def addVertex(self, label):
        self.nodesCount += 1
        self.verticies[label] = self.Vertex(label)


def maxFlow(f, t):
    f = g.verticies[f]
    t = g.verticies[t]
    visitedToken = 1
    flow = 0
    connections = {}

    def dfs(node, bootleneck=sys.maxsize):
        node.visitedToken = visitedToken
        bootleneck_backup = bootleneck

        if node == t:
            return bootleneck

        for edge in node.edges:
            if edge.remainingCapacity() == 0 or edge.to_.visitedToken == visitedToken:
                continue

            bootleneck = dfs(edge.to_, min(
                bootleneck, edge.remainingCapacity()))

            if bootleneck:
                if str(edge.from_.label).count(','):
                    connections[edge.from_.label] = edge.to_.label

                edge.augment(bootleneck)
                return bootleneck
            else:
                bootleneck = bootleneck_backup

        return 0

    while True:
        bootleneck = dfs(f)

        if not bootleneck:
            break

        flow += bootleneck
        visitedToken += 1

    return (flow, connections)


g = Graph()
g.addEdge(2, 1, 1)
rsults = []
t = int(input())
for _ in range(t):
    a, b = tuple(map(int, input().split(' ')))

    g.addEdge('source', f'{a},{b}',  1)

    g.addEdge(f'{a},{b}', a+b, 1)
    g.addEdge(a+b, 'sink', 1)

    g.addEdge(f'{a},{b}', a-b, 1)
    g.addEdge(a-b, 'sink', 1)

    g.addEdge(f'{a},{b}', a*b, 1)
    g.addEdge(a*b, 'sink', 1)


flow, connections = maxFlow('source', 'sink')

if flow != t:
    print('impossible')
else:
    for pair in connections.keys():
        a, b = map(int, pair.split(','))
        res = connections[pair]

        if a+b == res:
            rsults.append(f'{a} + {b} = {res}')

        elif a-b == res:
            rsults.append(f'{a} - {b} = {res}')

        elif a*b == res:
            rsults.append(f'{a} * {b} = {res}')

    for rs in rsults:
        print(rs)
