# Задача 1.1: Реверс строки через стек
def reverse_string(s: str) -> str:
    
    """Запрещено: s[::-1], reversed(), ''.join(reversed(s))"""
    stack = []
    # Push всех символов в стек
    for char in s:
        stack.append(char)
    
    reversed_s = ""
    # Pop до пустоты стека
    while stack:
        reversed_s += stack.pop()
    return reversed_s

# Задача 1.2: Очередь из двух стеков
class QueueFromStacks:
    """Очередь, реализованная с помощью двух стеков."""

    def __init__(self) -> None:
        """Инициализация двух стеков."""
        self.stack_in: list = []
        self.stack_out: list = []
    
    def enqueue(self, item) -> None:
        """Добавляет элемент в конец очереди."""
        self.stack_in.append(item)
    
    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди. Возвращает None, если очередь пуста."""
        if not self.stack_in and not self.stack_out:
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
