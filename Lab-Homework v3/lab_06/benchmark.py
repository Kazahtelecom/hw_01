import csv
import time
from heap_sort import heap_sort

def measure_time(sort_func, data, runs=3):
    times = []
    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sort_func(data_copy)
        times.append(time.perf_counter() - start)
    return sum(times) / len(times)

# 1. Загрузка данных из CSV
filename = 'gggg'# тут должен быть Тикет, но я не могу его загрузить его в гитхаб по этому оставляю так
all_costs = []

print(f"Читаю данные из {filename}...")
try:
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Преобразуем стоимость в число
            all_costs.append(int(row['cost']))
except FileNotFoundError:
    print(f"Файл {filename} не найден!")
    exit()

# 2. Тестирование на разных объемах данных из файла
# Не берем сразу миллион, чтобы не ждать вечность
sizes = [1000, 5000, 10000] 

print(f"{'n':>7} | {'heap_sort':>12} | {'sorted()':>12}")
print("-" * 40)

for size in sizes:
    if len(all_costs) < size:
        break
        
    data_sample = all_costs[:size]
    
    t_heap = measure_time(heap_sort, data_sample)
    t_sorted = measure_time(sorted, data_sample)

    print(f"{size:>7} | {t_heap:10.4f}s | {t_sorted:10.4f}s")