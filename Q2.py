from collections import deque

graph = {
    "Alice": ["Bob", "Claire", "Frank"],
    "Bob": ["Alice", "Dennis", "Eve"],
    "Claire": ["Alice", "Eve"],
    "Dennis": ["Bob"],
    "Eve": ["Bob", "Claire", "Frank"],
    "Frank": ["Alice", "Eve"],
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for friend in graph.get(node, []):
            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])
    return None

print(bfs("Alice", "Dennis"))
