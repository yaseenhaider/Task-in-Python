def dfs_maze(maze, start, end):
    stack = [start]
    visited = set()
    path = []

    while stack:
        current = stack.pop()
        if current == end:
            path.append(current)
            return path

        if current not in visited:
            visited.add(current)
            path.append(current)

            # neighbors up down left right
            for neighbor in get_neighbors(current, maze):
                if neighbor not in visited:
                    stack.append(neighbor)

            # break track krty hy condition k ziryyy
            if not any(neighbor not in visited for neighbor in get_neighbors(current, maze)):
                path.pop()
    return "No path found"


def get_neighbors(position, maze):
    x, y = position
    neighbors = []

    # Right, Down, Left, Up
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    #check valid neighuber
    for dx, dy in directions:
        if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
            neighbors.append((x + dx, y + dy))
    return neighbors



maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],

]
start = (0, 0)
end = (4, 4)
print(dfs_maze(maze, start, end))