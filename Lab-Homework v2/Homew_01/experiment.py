import time
import random

def has_duplicates_slow(lst): # O(n^2)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]: return True
    return False

def has_duplicates_fast(lst): # O(n) через хеш-таблицу (set)
    seen = set()
    for item in lst:
        if item in seen: return True
        seen.add(item)
    return False

for n in [1000, 10000, 100000]:
    test_data = [random.randint(0, n*2) for _ in range(n)]
    
    start = time.time()
    has_duplicates_fast(test_data)
    t_fast = time.time() - start
    
    t_slow = "-"
    if n <= 10000:
        start = time.time()
        has_duplicates_slow(test_data)
        t_slow = time.time() - start
    
    print(f"N={n}: O(n)={t_fast:.4f}s, O(n^2)={t_slow}")