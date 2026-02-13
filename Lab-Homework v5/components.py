from collections import deque


def find_components(graph):
    """Найти компоненты связности."""

    visited = set()
    components = []

    for start in graph.vertices():

        if start not in visited:

            component = set()
            queue = deque([start])
            visited.add(start)

            while queue:

                v = queue.popleft()
                component.add(v)

                for neighbor in graph.neighbors(v):

                    if neighbor not in visited:

                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components
