import time
import random

def find_duplicates_slow(lst): # O(n^2)
    dups = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in dups:
                dups.append(lst[i])
    return dups

def find_duplicates_fast(lst): # O(n)
    seen = set()
    dups = set()
    for item in lst:
        if item in seen:
            dups.add(item)
        else:
            seen.add(item)
    return list(dups)

def run_experiment():
    for n in [1000, 10000, 100000]:
        data = [random.randint(0, n) for _ in range(n)]
        
        # Замер O(n)
        s = time.perf_counter()
        find_duplicates_fast(data)
        t_fast = time.perf_counter() - s
        
        # Замер O(n^2) - только для малых N
        t_slow = 0
        if n <= 10000:
            s = time.perf_counter()
            find_duplicates_slow(data)
            t_slow = time.perf_counter() - s
            accel = t_slow / t_fast if t_fast > 0 else 0
            print(f"N={n:6} | O(n)={t_fast:.5f}s | O(n^2)={t_slow:.5f}s | Ускорение: {accel:.1f}x")
        else:
            print(f"N={n:6} | O(n)={t_fast:.5f}s | O(n^2)=Слишком долго | Ускорение: ---")

if __name__ == "__main__":
    run_experiment()