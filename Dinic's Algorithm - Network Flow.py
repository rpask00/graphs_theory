import heapq
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


g.addEdge(0, 1, 6)
g.addEdge(0, 2, 14)
g.addEdge(1, 2, 1)
g.addEdge(1, 3, 5)
g.addEdge(2, 3, 7)
g.addEdge(2, 4, 10)
g.addEdge(3, 5, 11)
g.addEdge(4, 5, 12)


def maxFlow(f, t):
    f = g.verticies[f]
    t = g.verticies[t]
    flow = 0

    def dfs(node, bootleneck=sys.maxsize):
        bootleneck_backup = bootleneck
        node.visited = True

        if node == t:
            return bootleneck

        heap = []

        for edge in node.edges:
            if not edge.remainingCapacity() or edge.to_.visited:
                continue

            heapq.heappush(heap, (-edge.remainingCapacity(), edge))

        while heap:
            maxCapacity, edge = heapq.heappop(heap)
            maxCapacity *= -1

            bootleneck = dfs(edge.to_, min(bootleneck, maxCapacity))

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
        g.markAllVerticiesAsNotVisited()
        
    return flow


print(maxFlow(0, 5))
