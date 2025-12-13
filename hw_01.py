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