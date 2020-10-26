class Graph:
    verticies = {}
    nodesCount = 0

    class Vertex:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.incoming = 0
            self.outcoming = 0

    class Edge:
        def __init__(self, from_, to_):
            self.from_ = from_
            self.to_ = to_
            self.visited = False

    def addEdge(self, from_, to_):
        self.verticies[from_].outcoming += 1
        self.verticies[to_].incoming += 1

        self.verticies[from_].edges.append(
            self.Edge(self.verticies[from_], self.verticies[to_]))

    def addVertex(self, label):
        self.nodesCount += 1
        self.verticies[label] = self.Vertex(label)

    def EulerianCircuitcanMount(self):
        for key in self.verticies:
            if self.verticies[key].incoming != self.verticies[key].outcoming:
                return False
        return True

    def EulerianPathStartingPoint(self):
        startingPoint = None
        outMore = 0
        inMore = 0

        for key in self.verticies:
            if self.verticies[key].incoming == self.verticies[key].outcoming:
                continue

            if self.verticies[key].incoming - self.verticies[key].outcoming == 1:
                inMore += 1
            elif self.verticies[key].outcoming - self.verticies[key].incoming == 1:
                outMore += 1
                startingPoint = key
            else:
                return False

        if inMore > 1 or outMore > 1:
            return False

        if inMore == outMore:
            return startingPoint if startingPoint else 1

        return False


g = Graph()

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)

g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 2)
g.addEdge(2, 4)
g.addEdge(2, 4)
g.addEdge(3, 2)
g.addEdge(3, 1)
g.addEdge(3, 5)
# g.addEdge(4, 6)
g.addEdge(4, 3)
g.addEdge(4, 1)
g.addEdge(5, 6)
g.addEdge(6, 3)


def EulerianPath():
    sp = g.EulerianPathStartingPoint()
    if sp is None:
        return []

    order = []

    def dfs(node):
        for edge in node.edges  :
            if edge.visited:
                continue

            edge.visited = True
            dfs(edge.to_)

        order.append(node.label)

    dfs(g.verticies[sp])

    order.reverse()
    return order


print(EulerianPath())
