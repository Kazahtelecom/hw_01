def find_common_naive(arr1, arr2):
    """
    Наивный подход: O(n * m)
    Для каждого элемента arr1 проверяем, есть ли он в arr2
    """
    common = []
    for item in arr1:
        if item in arr2 and item not in common:
            common.append(item)
    return common

def find_common_set(arr1, arr2):
    """
    Подход с множествами: O(n + m)
    Используем встроенную операцию пересечения множеств
    """
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)