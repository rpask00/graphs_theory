import sys


class Graph:
    verticies = {}
    nodesCount = 0

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
        from_ = self.verticies[from_]
        to_ = self.verticies[to_]

        main = self.Edge(from_, to_, False, capacity)
        residual = self.Edge(to_, from_, True, 0)

        main.residual = residual
        residual.residual = main

        from_.edges.append(main)
        to_.edges.append(residual)

    def addVertex(self, label):
        self.nodesCount += 1
        self.verticies[label] = self.Vertex(label)


g = Graph()
g.addVertex(0)
g.addVertex(23)

holes = [1, 4, 7, 9, 13, 15, 18, 21, 22]

for i in range(1, 23):
    g.addVertex(i)

for i in range(1, 23):
    if i not in holes:
        g.addEdge(0, i, 1)

g.addEdge(2, 1, 1)
g.addEdge(2, 4, 1)
g.addEdge(3, 4, 1)
g.addEdge(5, 4, 1)
g.addEdge(6, 4, 1)
g.addEdge(8, 4, 1)
g.addEdge(6, 7, 1)
g.addEdge(8, 7, 1)
g.addEdge(8, 9, 1)
g.addEdge(10, 9, 1)
g.addEdge(10, 22, 1)
g.addEdge(11, 22, 1)
g.addEdge(16, 15, 1)
g.addEdge(14, 15, 1)
g.addEdge(17, 15, 1)
g.addEdge(17, 18, 1)
g.addEdge(19, 18, 1)
g.addEdge(14, 13, 1)
g.addEdge(12, 13, 1)

g.addEdge(1, 23, 1)
g.addEdge(4, 23, 3)
g.addEdge(9, 23, 2)
g.addEdge(7, 23, 1)
g.addEdge(15, 23, 2)
g.addEdge(13, 23, 1)
g.addEdge(22, 23, 1)
g.addEdge(21, 23, 2)
g.addEdge(18, 23, 1)


def maxFlow(f, t):
    f = g.verticies[f]
    t = g.verticies[t]
    visitedToken = 1
    flow = 0

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

    return flow


print(maxFlow(0, 23))
