from functools import lru_cache


def find_common_routes_fast(tickets, active_routes):
    """Найти билеты на активных маршрутах (БЫСТРО)."""
    active_set = set(active_routes)   # O(m)
    result = []

    for ticket in tickets:            # O(n)
        if ticket['route_id'] in active_set:  # O(1)
            result.append(ticket)

    return result

def build_route_index(tickets):
    """
    Построение индекса маршрутов.
    Сложность: O(n)
    """
    index = {}

    for ticket in tickets:
        route = ticket['route_id']
        if route not in index:
            index[route] = []
        index[route].append(ticket)

    return index


def get_tickets_by_route_fast(index, route_id):
    """Поиск билетов по маршруту: O(1)"""
    return index.get(route_id, [])

@lru_cache(maxsize=100)
def route_stats(route_id):
    """
    Пример дорогого вычисления статистики маршрута.
    """
    total = 0
    for i in range(1_000_000):
        total += (i * route_id) % 7
    return total