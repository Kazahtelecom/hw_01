#import random

#def heapify(arr, n, i):
    #large = i  # Инициализируем наибольший как корень
    #left = 2 * i + 1     # левый = 2*i + 1
    #right = 2 * i + 2    # правый = 2*i + 2

    #if left < n and arr[left] > arr[large]: # Если левый дочерний элемент больше корня

        #large = left
    #if right < n and arr[right] > arr[large]: # Если правый дочерний элемент больше, чем самый большой элемент на данный момент

        #large = right
    #if large != i:
        #arr[i], arr[large] = arr[large], arr[i]  # обмен
        #heapify(arr, n, large) # Рекурсивно просеять вниз затронутое поддерево


    #pass

#def heap_sort(arr):
    #"""Сортировка кучей (in-place, возвращает arr)."""
   # n = len(arr)

    # Построение кучи
    #for i in range(n // 2 - 1, -1, -1):
        #heapify(arr, n, i)

    # Извлечение элементов
    #for i in range(n - 1, 0, -1):
       #arr[i], arr[0] = arr[0], arr[i]
        #heapify(arr, i, 0)
    
    #return arr

# Тесты для проверки


#def test_heap_sort():
    # Пустой массив
    #assert heap_sort([]) == []
    
    # Один элемент
    #assert heap_sort([42]) == [42]
    
    # Уже отсортирован
    #assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Обратный порядок
    #assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Случайные данные
    #data = [random.randint(0, 10000) for _ in range(1000)]
    #assert heap_sort(data.copy()) == sorted(data)
    
    #print("✓ Все тесты пройдены!")

#if __name__ == "__main__":
    #test_heap_sort()


import random
import time
import sys
from functools import wraps

# Увеличиваем лимит рекурсии для Merge Sort на очень больших списках
sys.setrecursionlimit(2000000)

# --- ВАШИ РЕАЛИЗАЦИИ ---

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break # Оптимизация: если перестановок не было, массив отсортирован
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Слияние
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- ЭКСПЕРИМЕНТ ---

def run_sorting_experiment():
    sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    # Ограничения: не запускать квадратичные сортировки на данных > 10K
    algorithms = [
        ("heap_sort", heap_sort, 1000000),
        ("sorted()", sorted, 1000000),
        ("merge_sort", merge_sort, 1000000),
        ("bubble_sort", bubble_sort, 10000),
        ("insertion_sort", insertion_sort, 10000)
    ]
    
    print(f"{'Алгоритм':<15} | {'1K':<10} | {'10K':<10} | {'100K':<10} | {'1M':<10}")
    print("-" * 65)

    for name, func, limit in algorithms:
        row = f"{name:<15}"
        for size in [1000, 10000, 100000, 1000000]:
            if size <= limit:
                # Генерируем случайные данные для каждого теста
                data = [random.randint(0, size * 10) for _ in range(size)]
                
                start = time.perf_counter()
                func(data)
                elapsed = time.perf_counter() - start
                
                row += f" | {elapsed:>8.4f}s"
            else:
                row += f" | {'timeout':>9}"
        print(row)

if __name__ == "__main__":
    run_sorting_experiment()
