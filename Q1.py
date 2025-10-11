# Simple DFS Maze Solver
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)
dirs = [(1,0), (0,1), (-1,0), (0,-1)]

def in_bounds(r, c):
    return 0 <= r < len(maze) and 0 <= c < len(maze[0])

def dfs(r, c, path, visited):
    if not in_bounds(r, c) or maze[r][c] == 1 or (r, c) in visited:
        return False
    path.append((r, c))
    visited.add((r, c))
    if (r, c) == goal:
        return True
    for dr, dc in dirs:
        if dfs(r+dr, c+dc, path, visited):
            return True
    path.pop()
    return False

path, visited = [], set()
if dfs(start[0], start[1], path, visited):
    for r, c in path:
        maze[r][c] = '*'
    maze[start[0]][start[1]] = 'S'
    maze[goal[0]][goal[1]] = 'G'
    for row in maze:
        print(' '.join(str(x) for x in row))
    print("Path:", path)
else:
    print("No path found.")
