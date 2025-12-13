import time
import random

# Генерация данных
n = 100000
data = [random.randint(1, n // 2) for _ in range(n)]
target = random.choice(data)

start = time.time()
target in data 
end = time.time()
list_time = end - start

data_set = set(data)

start = time.time()
target in data_set 
end = time.time()
set_time = end - start

print(f"Time taken to search in list: {list_time:.6f} seconds")
print(f"Time taken to search in set: {set_time:.6f} seconds")
print(f"Set search is {list_time / set_time:.2f} times faster than list search")
print(f"Data size: {n} elements")
print(f"Target value: {target}")




