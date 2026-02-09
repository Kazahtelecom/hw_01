def heap_sort(arr):
    """
    Сортировка кучей (in-place).
    """
    n = len(arr)

    # Шаг 1: построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Шаг 2: извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # перенос максимума в конец
        heapify(arr, i, 0)              # восстановление кучи

    return arr
