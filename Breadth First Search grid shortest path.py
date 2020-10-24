dungeon = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.'],
]

visited = [[False for i in range(len(row))] for row in dungeon]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r_que = []
c_que = []

width = len(dungeon[-1])
height = len(dungeon)

nodes_in_next_layer = 0
nodes_left_in_layer = 1


def wisitCells(r, c):
    visited[r][c] = True
    global nodes_in_next_layer

    for i in range(4):
        r_index = r + dr[i]
        c_index = c + dc[i]

        if r_index < 0 or c_index < 0:
            continue

        if r_index == height or c_index == width:
            continue

        print(r_index, c_index)
        if visited[r_index][c_index]:
            continue

        if dungeon[r_index][c_index] == '#':
            visited[r_index][c_index] = True
            continue

        r_que.append(r_index)
        c_que.append(c_index)

        visited[r_index][c_index] = True
        nodes_in_next_layer += 1


def shortestPath(sr, sc):
    r_que.append(sr)
    c_que.append(sc)
    visited[sr][sc] = True
    reached_end = False
    move_count = 0
    global nodes_left_in_layer, nodes_in_next_layer

    while len(r_que):
        r = r_que.pop(0)
        c = c_que.pop(0)
        if dungeon[r][c] == 'E':
            reached_end = True
            break

        wisitCells(r, c)
        nodes_left_in_layer -= 1
        if not nodes_left_in_layer:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    return move_count if reached_end else -1


print(shortestPath(0, 0))
