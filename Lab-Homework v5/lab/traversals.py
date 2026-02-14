from collections import deque


def bfs(graph, start):
    """Обход в ширину. Вернуть список вершин в порядке посещения."""
    
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:

        v = queue.popleft()
        order.append(v)

        for neighbor in graph.neighbors(v):

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return order



def dfs(graph, start):
    """Обход в глубину (итеративный)."""

    visited = set()
    stack = [start]
    order = []

    while stack:

        v = stack.pop()

        if v not in visited:

            visited.add(v)
            order.append(v)

            # добавляем соседей в стек
            for neighbor in graph.neighbors(v):

                if neighbor not in visited:
                    stack.append(neighbor)

    return order



def shortest_path(graph, start, end):
    """Кратчайший путь через BFS."""

    if start == end:
        return [start]

    visited = set([start])
    queue = deque([start])
    parent = {}

    while queue:

        v = queue.popleft()

        for neighbor in graph.neighbors(v):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = v
                queue.append(neighbor)

                if neighbor == end:

                    # восстановление пути
                    path = []
                    cur = end

                    while cur != start:
                        path.append(cur)
                        cur = parent[cur]

                    path.append(start)
                    path.reverse()

                    return path

    return None