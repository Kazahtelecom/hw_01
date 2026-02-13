import random
import time
import cProfile


def find_common_routes_slow(tickets, active_routes):
    """Найти билеты на активных маршрутах (МЕДЛЕННО)."""
    result = []
    for ticket in tickets:
        for route in active_routes:
            if ticket['route_id'] == route:
                result.append(ticket)
                break
    return result


# Тестовые данные
tickets = [{'id': i, 'route_id': random.randint(1, 1000)}
           for i in range(100000)]
active_routes = list(range(1, 501))


# Измерение времени
start = time.perf_counter()
result = find_common_routes_slow(tickets, active_routes)
elapsed = time.perf_counter() - start
print(f"Время: {elapsed:.4f} сек, найдено: {len(result)}")


# Профилирование
cProfile.run('find_common_routes_slow(tickets, active_routes)')
