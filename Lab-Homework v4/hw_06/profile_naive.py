import random
import time
import cProfile
"Профилирование наивной реализации для сравнения с оптимизированной версией."
from native import (
    top_routes_by_revenue_naive,
    tickets_by_hour_naive,
    find_duplicates_naive
)
"№ Наивная реализация для сравнения с оптимизированной версией."
def generate_tickets(n):
    tickets = []
    for i in range(n):
        tickets.append({
            'from': random.choice(['A', 'B', 'C', 'D']),
            'to': random.choice(['E', 'F', 'G']),
            'price': random.randint(50, 500),
            'hour': random.randint(0, 23),
            'original_id': random.randint(1, n // 10)
        })
    return tickets

"Генерируем тестовые данные и запускаем функции для сравнения производительности."
tickets = generate_tickets(10_000)
"Проверяем производительность наивной реализации."
print("top_routes_by_revenue_naive:")
start = time.perf_counter()
top_routes_by_revenue_naive(tickets)
print(time.perf_counter() - start)

print("tickets_by_hour_naive:")
start = time.perf_counter()
tickets_by_hour_naive(tickets)
print(time.perf_counter() - start)

print("find_duplicates_naive:")
start = time.perf_counter()
find_duplicates_naive(tickets)
print(time.perf_counter() - start)

print("\n=== cProfile find_duplicates_naive ===")
cProfile.run("find_duplicates_naive(tickets)")
