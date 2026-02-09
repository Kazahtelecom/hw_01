def heapify(arr, n, i):
    """
    Просеивание вниз для max-heap.
    
    arr: массив
    n: размер кучи
    i: индекс узла
    """
    largest = i          # предполагаем, что корень — самый большой
    left = 2 * i + 1     # левый потомок
    right = 2 * i + 2    # правый потомок

    # Если левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок больше текущего максимума
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если самый большой не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Рекурсивно просеиваем дальше
        heapify(arr, n, largest)
