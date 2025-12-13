import random
import time



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

def main():
    """
    The main function for generating data, measuring performance, and writing results to a file
    """
    size = 50000
    max_value = 30000
    arr1 = [random.randint(0, max_value) for _ in range(size)]
    arr2 = [random.randint(0, max_value) for _ in range(size)]
    print ("Array sizes", size "elements each")
    

    start_time = time.time()
    common_naive = find_common_naive(arr1, arr2)
    naive_time = time.time() - start_time

    start_time = time.time()
    common_set = find_common_set(arr1, arr2)
    set_time = time.time() - start_time
    
    is_correct = set(common_naive) == set(common_set)

    with open("results.txt", "w") as f:
        f.write(f"Naive approach time: {naive_time:.6f} seconds\n")
        f.write(f"Set approach time: {set_time:.6f} seconds\n")
        f.write(f"Results are the same: {is_correct}\n")
    print("Results written to results.txt")
# Output results to the screen
    print(f"Naive approach time: {naive_time:.6f} seconds")
    print(f"Set approach time: {set_time:.6f} seconds")
    print(f"Results are the same: {is_correct}")
