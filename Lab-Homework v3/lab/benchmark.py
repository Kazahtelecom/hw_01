import random

# Тест 1: случайный массив
data = [random.randint(0, 1000) for _ in range(100)]
result = heap_sort(data.copy())
assert result == sorted(data), "Ошибка на случайных данных!"

# Тест 2: уже отсортированный
data = list(range(100))
result = heap_sort(data.copy())
assert result == sorted(data)

# Тест 3: обратный порядок
data = list(range(100, 0, -1))
result = heap_sort(data.copy())
assert result == sorted(data)

print("✓ Все тесты пройдены!")
