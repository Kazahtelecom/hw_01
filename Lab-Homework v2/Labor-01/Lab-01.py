from collections import deque


class Stack:
    def __init__(self):
        # Использование приватного списка для хранения элементов
        self._items = []
    
    def push(self, item):
        """Добавить элемент на вершину (O(1))."""
        self._items.append(item)
    
    def pop(self):
        """Удалить и вернуть элемент с вершины (O(1))."""
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self._items.pop()
    
    def peek(self):
        """Вернуть вершину без удаления (O(1))."""
        if self.is_empty():
            return None
        return self._items[-1]
    
    def is_empty(self):
        """Проверить пустоту (O(1))."""
        return len(self._items) == 0
    
    from collections import deque

class Queue:
    def __init__(self):
        # Использование двусторонней очереди для эффективности
        self._items = deque()
    
    def enqueue(self, item):
        """Добавить в конец (O(1))."""
        self._items.append(item)
    
    def dequeue(self):
        """Извлечь из начала (O(1))."""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items.popleft()
    
    def is_empty(self):
        """Проверить пустоту (O(1))."""
        return len(self._items) == 0
def is_balanced(expression):
    """
    Проверяет баланс скобок: (), [], {}
    Использует стек для сопоставления пар.
    """
    stack = []
    # Словарь соответствия закрывающей скобки к открывающей
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "([{":
            # Если скобка открывающая — push в стек
            stack.append(char)
        elif char in ")]}":
            # Если стек пуст или скобки не совпали — дисбаланс
            if not stack or stack.pop() != pairs[char]:
                return False
    
    # Если в конце стек пуст — все скобки закрыты правильно
    return len(stack) == 0

# Тесты
print(is_balanced("{[()]}")) # True
print(is_balanced("{[(])}")) # False