from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        """Добавить в конец (O(1))."""
        self._items.append(item)
    
    def dequeue(self):
        """Извлечь из начала (O(1))."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()
    
    def is_empty(self):
        return len(self._items) == 0
    def size(self):
        """Вернуть количество элементов в очереди."""
        return len(self._items)
# Тестирование очереди
if __name__ == "__main__":
    q = Queue()
    q.enqueue("Первый")
    q.enqueue("Второй")
    print(f"Извлечено: {q.dequeue()}") # Ожидаем: Первый (принцип FIFO)
    print(f"Осталось в очереди: {q.size()}")
    print(f"Извлечено: {q.dequeue()}") # Ожидаем: Второй
    print(f"Очередь пуста: {q.is_empty()}")