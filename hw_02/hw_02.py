import random
import time

def find_common_naive(arr1, arr2):
    """
    Naive approach: O(n * m)
    For each element in arr1, check if it exists in arr2
    """
    common = []
    for item in arr1:
        if item in arr2 and item not in common:
            common.append(item)
    return common

def find_common_set(arr1, arr2):
    """
    Optimized set approach: O(n + m)
    Uses built-in set intersection operation
    """
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)

def main():
    """
    Main function for data generation, performance measurement, and results writing
    """
    size = 50000
    max_value = 30000
    
    # Generate test data
    arr1 = [random.randint(1, max_value) for _ in range(size)]
    arr2 = [random.randint(1, max_value) for _ in range(size)]
    
    print(f"Array sizes: {size} each")
    print(f"Value range: 1 - {max_value}")
    print(f"Running naive approach (may take a while)...")
    
    # Measure naive approach
    start_time = time.perf_counter()  # More precise than time.time()
    common_naive = find_common_naive(arr1, arr2)
    naive_time = time.perf_counter() - start_time
    
    # Measure set approach
    start_time = time.perf_counter()
    common_set = find_common_set(arr1, arr2)
    set_time = time.perf_counter() - start_time
    
    # Verify results match
    is_correct = set(common_naive) == set(common_set)
    
    # Calculate speedup
    if set_time > 0:
        speedup = naive_time / set_time
    else:
        speedup = float('inf')
    
    # Write to file
        # Write to file in required format
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("========================================\n")
        f.write("ДОМАШНЕЕ ЗАДАНИЕ 1 — РЕЗУЛЬТАТЫ\n")
        f.write("========================================\n\n")

        f.write(f"Размер array1: {size}\n")
        f.write(f"Размер array2: {size}\n")
        f.write(f"Диапазон значений: 1-{max_value}\n\n")

        f.write("ПОДХОД 1: НАИВНЫЙ (вложенные циклы)\n")
        f.write("-------------------------------------\n")
        f.write(f"Время выполнения: {naive_time:.4f} секунд\n")
        f.write(f"Найдено общих элементов: {len(common_naive)}\n\n")

        f.write("ПОДХОД 2: МНОЖЕСТВА (set intersection)\n")
        f.write("---------------------------------------\n")
        f.write(f"Время выполнения: {set_time:.4f} секунд\n")
        f.write(f"Найдено общих элементов: {len(common_set)}\n\n")

        f.write("СРАВНЕНИЕ\n")
        f.write("---------\n")
        f.write(f"Ускорение: {speedup:.1f} раз\n\n")

        f.write("ОБЪЯСНЕНИЕ РАЗНИЦЫ В ПРОИЗВОДИТЕЛЬНОСТИ:\n")
        f.write(
            "Наивный подход использует вложенные циклы и проверяет каждый элемент "
            "первого массива на наличие во втором массиве с помощью линейного поиска. "
            "Это приводит к квадратичной временной сложности O(n*m), что при больших "
            "размерах массивов вызывает резкое увеличение времени выполнения. "
            "Подход с использованием множеств преобразует массивы в структуры данных "
            "с хешированием, где проверка наличия элемента выполняется в среднем за O(1). "
            "Благодаря этому общая сложность снижается до O(n+m), что обеспечивает "
            "значительное ускорение работы программы.\n\n"
        )

        f.write("========================================\n")

        

        
    
    # Output to screen
    print(f"\n=== RESULTS ===")
    print(f"Naive approach: {naive_time:.3f} seconds")
    print(f"Set approach: {set_time:.6f} seconds")
    print(f"Speedup: {speedup:.1f}x faster")
    print(f"Results match: {is_correct}")
    print(f"Common elements found: {len(common_set)}")
    print(f"\nResults written to: results.txt")


if __name__ == "__main__":
    main()