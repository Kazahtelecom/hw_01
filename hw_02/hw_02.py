import random
import time

def find_common_naive(arr1, arr2):
    """
    Naive approach: O(n * m)
    For each element in arr1, check if it exists in arr2
    """
    common = []
    for item in arr1:
        if item in arr2 and item not in common:
            common.append(item)
    return common

def find_common_set(arr1, arr2):
    """
    Optimized set approach: O(n + m)
    Uses built-in set intersection operation
    """
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)

def main():
    """
    Main function for data generation, performance measurement, and results writing
    """
    size = 50000
    max_value = 30000
    
    # Generate test data
    arr1 = [random.randint(1, max_value) for _ in range(size)]
    arr2 = [random.randint(1, max_value) for _ in range(size)]
    
    print(f"Array sizes: {size} each")
    print(f"Value range: 1 - {max_value}")
    print(f"Running naive approach (may take a while)...")
    
    # Measure naive approach
    start_time = time.perf_counter()  # More precise than time.time()
    common_naive = find_common_naive(arr1, arr2)
    naive_time = time.perf_counter() - start_time
    
    # Measure set approach
    start_time = time.perf_counter()
    common_set = find_common_set(arr1, arr2)
    set_time = time.perf_counter() - start_time
    
    # Verify results match
    is_correct = set(common_naive) == set(common_set)
    
    # Calculate speedup
    if set_time > 0:
        speedup = naive_time / set_time
    else:
        speedup = float('inf')
    
    # Write to file
    with open("results.txt", "w") as f:
        f.write(f"Naive approach time: {naive_time:.6f} seconds\n")
        f.write(f"Set approach time: {set_time:.6f} seconds\n")
        f.write(f"Speedup: {speedup:.1f}x faster\n")
        f.write(f"Results are the same: {is_correct}\n")
        f.write(f"1. Naive approach has O(n*m) complexity:\n")
        f.write(f"   • 50,000 * 50,000 = 2,500,000,000 operations\n")
        f.write(f"   • Each 'item in arr2' requires linear search\n\n")
        f.write(f"2. Set approach has O(n + m) complexity:\n")
        f.write(f"   • 50,000 + 50,000 = 100,000 operations\n")
        f.write(f"   • Set lookups are on average O(1)\n")

        f.write(f"3. Speed difference:\n")
        f.write(f"   • Naive: {naive_time:.6f} seconds\n")
        f.write(f"   • Set: {set_time:.6f} seconds\n")
        f.write(f"   • Speedup: {speedup:.1f}x faster\n")
        

        
    
    # Output to screen
    print(f"\n=== RESULTS ===")
    print(f"Naive approach: {naive_time:.3f} seconds")
    print(f"Set approach: {set_time:.6f} seconds")
    print(f"Speedup: {speedup:.1f}x faster")
    print(f"Results match: {is_correct}")
    print(f"Common elements found: {len(common_set)}")
    print(f"\nResults written to: results.txt")


if __name__ == "__main__":
    main()