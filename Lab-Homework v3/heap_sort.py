import random

def heapify(arr, n, i):
    """Просеивание вниз для max-heap."""
    # Ваша реализация
    large = i  # Инициализируем наибольший как корень
    left = 2 * i + 1     # левый = 2*i + 1
    right = 2 * i + 2    # правый = 2*i + 2

    if left < n and arr[left] > arr[large]: # Если левый дочерний элемент больше корня

        large = left
    if right < n and arr[right] > arr[large]: # Если правый дочерний элемент больше, чем самый большой элемент на данный момент

        large = right
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]  # обмен
        heapify(arr, n, large) # Рекурсивно просеять вниз затронутое поддерево


    pass

def heap_sort(arr):
    """Сортировка кучей (in-place, возвращает arr)."""
    n = len(arr)

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

# Тесты для проверки


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

if __name__ == "__main__":
    test_heap_sort()
