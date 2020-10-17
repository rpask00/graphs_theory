import sys


class Graph:
    class Edge:
        def __init__(self, from_, to_, weight):
            self.from_ = from_
            self.to_ = to_
            self.weight = weight

    edges = []
    verticies = set()

    def addEdge(self, from_, to_, weight):
        self.verticies.add(from_)
        self.verticies.add(to_)
        self.edges.append(self.Edge(from_, to_, weight))


g = Graph()
g.addEdge(0, 1, 5)
g.addEdge(1, 2, 20)
g.addEdge(1, 5, 30)
g.addEdge(1, 6, 60)
g.addEdge(2, 3, 10)
g.addEdge(2, 4, 75)
g.addEdge(3, 2, -15)
g.addEdge(4, 9, 100)
g.addEdge(5, 4, 25)
g.addEdge(5, 6, 5)
g.addEdge(5, 8, 50)
g.addEdge(6, 7, -50)
g.addEdge(7, 8, -10)


D = [sys.maxsize for _ in range(len(g.verticies))]


def bf(start):
    D[start] = 0
    for _ in range(len(g.verticies)-1):
        for edge in g.edges:
            if D[edge.to_] > D[edge.from_] + edge.weight:
                D[edge.to_] = D[edge.from_] + edge.weight

    return negative_cycle_detection()


def negative_cycle_detection():
    for _ in range(len(g.verticies)-1):
        for edge in g.edges:
            if D[edge.to_] > D[edge.from_] + edge.weight:
                D[edge.to_] = -sys.maxsize

    return D


print(bf(0))
