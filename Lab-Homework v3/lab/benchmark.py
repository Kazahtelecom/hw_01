import random
import time
from heap_sort import heap_sort


def measure_time(sort_func, data, runs=5):
    times = []
    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sort_func(data_copy)
        times.append(time.perf_counter() - start)
    return sum(times) / len(times)


sizes = [1000, 5000, 10000]

for size in sizes:
    data = [random.randint(0, 100000) for _ in range(size)]

    t_heap = measure_time(heap_sort, data)
    t_sorted = measure_time(sorted, data)

    print(f"n={size}: heap_sort={t_heap:.4f}s, sorted={t_sorted:.4f}s")
