def top_routes_by_revenue_naive(tickets, n=10):
    """
    TOP-N маршрутов по выручке.
    Наивная реализация: O(m × n)
    """
    routes = []

    for t in tickets:
        route = (t['from'], t['to'])
        if route not in routes:
            routes.append(route)

    revenues = []
    for route in routes:
        total = 0
        for t in tickets:
            if (t['from'], t['to']) == route:
                total += t['price']
        revenues.append((route, total))

    revenues.sort(key=lambda x: x[1], reverse=True)
    return revenues[:n]


def tickets_by_hour_naive(tickets):
    """
    Количество билетов по часам (0–23).
    """
    result = {}
    for hour in range(24):
        count = 0
        for t in tickets:
            if t['hour'] == hour:
                count += 1
        result[hour] = count
    return result


def find_duplicates_naive(tickets, key='original_id'):
    """
    Найти дубликаты по ключу.
    Наивная реализация: O(n²)
    """
    # Ваш код
    pass