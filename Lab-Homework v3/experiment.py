import time
import random
from heap_sort import heap_sort
from other_sorts import bubble_sort, insertion_sort, merge_sort

def benchmark(func, data):
    start = time.perf_counter()
    func(data.copy())
    return time.perf_counter() - start

def run_experiment():
    sizes = [1000, 10000, 100000, 1000000]
    results = {}

    for size in sizes:
        print(f"Тестируем размер: {size}...")
        data = [random.randint(0, size * 10) for _ in range(size)]
        
        results[size] = {
            "heap": benchmark(heap_sort, data),
            "sorted": benchmark(sorted, data),
            "merge": benchmark(merge_sort, data)
        }
        
        # Квадратичные только до 10к
        if size <= 10000:
            results[size]["bubble"] = benchmark(bubble_sort, data)
            results[size]["insertion"] = benchmark(insertion_sort, data)
        else:
            results[size]["bubble"] = "timeout"
            results[size]["insertion"] = "timeout"

    # Вывод таблицы в консоль (для копирования в отчет)
    print(f"\n{'Алгоритм':<15} | {'1K':<10} | {'10K':<10} | {'100K':<10} | {'1M':<10}")
    for alg in ["heap", "sorted", "merge", "bubble", "insertion"]:
        row = f"{alg:<15}"
        for size in sizes:
            val = results[size].get(alg)
            res = f"{val:.4f}s" if isinstance(val, float) else val
            row += f" | {res:<10}"
        print(row)

if __name__ == "__main__":
    run_experiment()