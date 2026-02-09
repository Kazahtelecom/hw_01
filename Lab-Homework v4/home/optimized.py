
import heapq

def top_routes_by_revenue_fast(tickets, n=10):
    revenue = {}  # обычный словарь

    for t in tickets:
        route = (t['from'], t['to'])
        if route in revenue:
            revenue[route] += t['price']
        else:
            revenue[route] = t['price']

    return heapq.nlargest(n, revenue.items(), key=lambda x: x[1])

def tickets_by_hour_fast(tickets):
    result = {}

    for t in tickets:
        hour = t['hour']
        if hour in result:
            result[hour] += 1
        else:
            result[hour] = 1

    return result

def find_duplicates_fast(tickets, key='original_id'):
    seen = set()
    duplicates = []

    for t in tickets:
        value = t[key]
        if value in seen:
            duplicates.append(t)
        else:
            seen.add(value)

    return duplicates
