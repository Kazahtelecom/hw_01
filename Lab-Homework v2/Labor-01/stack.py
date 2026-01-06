class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Добавить элемент на вершину (O(1))."""
        self._items.append(item)
    
    def pop(self):
        """Удалить и вернуть элемент с вершины. Выбросить IndexError если пуст."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Вернуть вершину без удаления."""
        return self._items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        """Проверить пустоту."""
        return len(self._items) == 0
    
    def size(self):
        """Вернуть количество элементов в стеке."""
        return len(self._items) 
    