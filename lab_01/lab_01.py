import time
import random

def run_experiments():
    print(f"{'Size':>10} | {'List Time (s)':>15} | {'Set Time (s)':>15} | {'Speedup':>10}")
    print("-" * 60)
    for exp in range(1, 8):
        n = 10 ** exp
        data = [random.randint(1, n // 2) for _ in range(n)]
        target = random.choice(data)

        # Search in list
        start = time.perf_counter()
        target in data
        end = time.perf_counter()
        list_time = end - start

        # Search in set
        data_set = set(data)
        start = time.perf_counter()
        target in data_set
        end = time.perf_counter()
        set_time = end - start

        speedup = list_time / set_time if set_time > 0 else float('inf')
        print(f"{n:>10} | {list_time:>15.6f} | {set_time:>15.6f} | {speedup:>10.2f}")

# Генерация данных
n = 100000
data = [random.randint(1, n // 2) for _ in range(n)]
target = random.choice(data)

# Поиск в списке
start = time.perf_counter()
target in data 
end = time.perf_counter()
list_time = end - start

# Поиск в множестве
data_set = set(data)


start = time.perf_counter()
target in data_set 
end = time.perf_counter()
set_time = end - start
# Вывод результатов
print(f"Time taken to search in list: {list_time:.6f} seconds")
print(f"Time taken to search in set: {set_time:.6f} seconds")
print(f"Set search is {list_time / set_time:.2f} times faster than list search")
print(f"Data size: {n} elements")
print(f"Target value: {target}")




