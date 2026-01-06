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