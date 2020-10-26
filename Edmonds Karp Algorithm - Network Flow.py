import sys


class Graph:
    verticies = {}
    nodesCount = 0

    class Vertex:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.visited = False

        def markAsNotVisited(self):
            self.visited = False

        def visit(self):
            self.visited = True

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

    def markAllVerticiesAsNotVisited(self):
        for ver in self.verticies:
            self.verticies[ver].markAsNotVisited()


g = Graph()

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)


g.addEdge(0, 1, 5)
g.addEdge(0, 2, 10)
g.addEdge(0, 3, 5)
g.addEdge(2, 1, 15)
g.addEdge(1, 4, 10)
g.addEdge(2, 5, 20)
g.addEdge(3, 6, 10)
g.addEdge(4, 5, 25)
g.addEdge(4, 7, 10)
g.addEdge(5, 3, 5)
g.addEdge(5, 8, 30)
g.addEdge(6, 8, 5)
g.addEdge(7, 10, 5)
g.addEdge(8, 10, 15)
g.addEdge(8, 9, 5)
g.addEdge(8, 4, 15)
g.addEdge(9, 10, 10)


def maxFlow(f, t):
    f = g.verticies[f]
    t = g.verticies[t]
    flow = 0

    def bfs():
        prev = [None for _ in range(g.nodesCount)]
        que = [f]

        while que:
            node = que.pop(0)
            node.visit()

            if node == t:
                break

            for edge in node.edges:
                if edge.remainingCapacity() == 0 or edge.to_.visited:
                    continue

                prev[edge.to_.label] = edge
                que.append(edge.to_)

        if not prev[t.label]:
            return 0

        bootleneck = sys.maxsize

        edge = prev[t.label]
        while edge:
            bootleneck = min(bootleneck, edge.remainingCapacity())
            edge = prev[edge.from_.label]

        edge = prev[t.label]
        while edge:
            edge.augment(bootleneck)
            edge = prev[edge.from_.label]

        return bootleneck

    while True:
        bootleneck = bfs()
        if not bootleneck:
            break
        flow += bootleneck
        g.markAllVerticiesAsNotVisited()

    return flow


print(maxFlow(0, 5))
