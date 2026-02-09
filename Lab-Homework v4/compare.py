import time
import random

from native import *
from optimized import *

def generate_tickets(n):
    return [{
        'from': random.choice(['A', 'B', 'C']),
        'to': random.choice(['D', 'E']),
        'price': random.randint(100, 500),
        'hour': random.randint(0, 23),
        'original_id': random.randint(1, n // 10)
    } for _ in range(n)]


tickets = generate_tickets(10_000)

def measure(func, data):
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


print("top_routes_by_revenue:")
print("naive:", measure(top_routes_by_revenue_naive, tickets))
print("fast :", measure(top_routes_by_revenue_fast, tickets))

print("\ntickets_by_hour:")
print("naive:", measure(tickets_by_hour_naive, tickets))
print("fast :", measure(tickets_by_hour_fast, tickets))

print("\nfind_duplicates:")
print("naive:", measure(find_duplicates_naive, tickets))
print("fast :", measure(find_duplicates_fast, tickets))