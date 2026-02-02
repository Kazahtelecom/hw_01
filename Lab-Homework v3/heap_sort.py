import random


def heapify(arr, n, i):
    """Просеивание вниз для max-heap."""
    # Ваша реализация
    large = i  # Инициализируем наибольший как корень
    left = 2 * i + 1     # левый = 2*i + 1
    right = 2 * i + 2    # правый = 2*i + 2

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[large]:

        large = left
    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if right < n and arr[right] > arr[large]:

        large = right
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]  # обмен
        heapify(arr, n, large)  # Рекурсивно просеять вниз затронутое поддерево

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
