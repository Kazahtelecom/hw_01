# Задача 1.1: Реверс строки через стек
def reverse_string(s: str) -> str:
    """Запрещено: s[::-1], reversed()"""
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
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, item):
        self.stack_in.append(item)
    
    def dequeue(self):
        if not self.stack_in and not self.stack_out:
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
