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
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)


g.addEdge(0, 1, 10)
g.addEdge(0, 2, 10)
g.addEdge(1, 3, 25)
g.addEdge(2, 4, 15)
g.addEdge(4, 1, 6)
g.addEdge(3, 5, 10)
g.addEdge(4, 5, 10)


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
            
            bootleneck = dfs(edge.to_, min(bootleneck, edge.remainingCapacity()))
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


print(maxFlow(0, 5))
