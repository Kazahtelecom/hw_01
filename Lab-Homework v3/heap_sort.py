def heapify(arr, n, i):
    """Просеивание вниз для max-heap."""
    # Ваша реализация
    pass

def heap_sort(arr):
    """Сортировка кучей (in-place, возвращает arr)."""
    # Ваша реализация
    pass

# Тесты для проверки
import random

def test_heap_sort():
    # Пустой массив
    assert heap_sort([]) == []
    
    # Один элемент
    assert heap_sort([42]) == [42]
    
    # Уже отсортирован
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Обратный порядок
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Случайные данные
    data = [random.randint(0, 10000) for _ in range(1000)]
    assert heap_sort(data.copy()) == sorted(data)
    
    print("✓ Все тесты пройдены!")

test_heap_sort()