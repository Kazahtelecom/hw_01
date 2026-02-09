
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
