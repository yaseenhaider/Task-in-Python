from collections import deque

def bfs_social_network(graph, start, target):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]

                #revers path
            return path[::-1]


        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return "No connection found"


social_graph = {
    'Sunil': ['ali', 'hamza'],
    'ali': ['sunil', 'haider'],
    'hamza': ['sunil', 'mohsin'],
    'haider': ['ali', 'mohsin'],
    'mohsin': ['hamza', 'haider'],
}
start_user = 'sunil'
target_user = 'haider'
print(bfs_social_network(social_graph, start_user, target_user))

