class Stack:
    """Реализация стека с использованием списка Python."""

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


def is_balanced(expression):
    """Проверить, сбалансированы ли скобки в выражении."""
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False

    return stack.is_empty()


# Тестирование (Задание A3)
if __name__ == "__main__":
    test_cases = ["{[()]}", "{[(])}", "((()))", "[()]{}", "({[})"]

    print("--- Проверка баланса скобок ---")
    for expr in test_cases:
        result = is_balanced(expr)
        print(f"Выражение: {expr:10} | Сбалансировано: {result}")
