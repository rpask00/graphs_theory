graph = {
   'A': ['D'],
   'B': ['D'],
   'C': ['A', 'B'],
   'D': ['H', 'G'],
   'E': ['A', 'D', 'F'],
   'F': ['K', 'J'],
   'G': ['I'],
   'H': ['J', 'I'],
   'I': ['L'],
   'J': ['M', 'L'],
   'K': ['J'],
   'L': [],
   'M': [],

}
n = len(graph)

visited  = {
   'A':False,
   'B':False,
   'C':False,
   'D':False,
   'E':False,
   'F':False,
   'G':False,
   'H':False,
   'I':False,
   'J':False,
   'K':False,
   'L':False,
   'M':False,

}
ans = []


def topological_sort(l):
    if visited[l]:
        return

    visited[l] = True

    for nxt in graph[l]:
        if visited[nxt]:
            continue

        topological_sort(nxt)

    ans.append(l)


for lindex in graph:
    topological_sort(lindex)

ans.reverse()
print(ans)
