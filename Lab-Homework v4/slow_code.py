import random

def find_common_routes_slow(tickets, active_routes):
    """Найти билеты на активных маршрутах (МЕДЛЕННО)."""
    result = []
    for ticket in tickets:
        for route in active_routes:  # O(m)
            if ticket['route_id'] == route:
                result.append(ticket)
                break
    return result

# Тестовые данные
tickets = [{'id': i, 'route_id': random.randint(1, 1000)} 
           for i in range(100000)]
active_routes = list(range(1, 501))  # 500 маршрутов