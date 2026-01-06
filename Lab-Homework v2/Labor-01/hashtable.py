class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value) # Обновление
                return
        self.table[idx].append((key, value)) # Вставка
    
    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key: return v
        raise KeyError(key)

    def contains(self, key):
        idx = self._hash(key)
        return any(k == key for k, v in self.table[idx])

# Демонстрация коллизии
ht = SimpleHashTable(size=5)
# Находим ключи с одинаковым индексом: hash(key) % 5
# Например, 1 и 6 при размере 5 дадут индекс 1
ht.insert(1, "Value1")
ht.insert(6, "Value2")
print(f"Index for 1: {hash(1)%5}, Index for 6: {hash(6)%5}")
print(f"Chain at index 1: {ht.table[1]}") # Покажет оба элемента

print(ht.get(1))  # Вывод: Value1
print(ht.get(6))  # Вывод: Value2