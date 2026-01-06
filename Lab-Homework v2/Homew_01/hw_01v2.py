
def reverse_string(s: str) -> str:
    """Инверсия строки через стек (LIFO)."""
    stack = []
    for char in s:
        stack.append(char)  # push

    reversed_s = ''
    while stack:
        reversed_s += stack.pop()  # pop извлекает последний добавленный
    return reversed_s

class QueueFromStacks:
    """Очередь (FIFO) через два стека (LIFO)."""
    def __init__(self):
        self.stack_in = []   # Для добавления
        self.stack_out = []  # Для извлечения
    
    def enqueue(self, item):
        self.stack_in.append(item)
    
    def dequeue(self):
        if not self.stack_in and not self.stack_out:
            return None 
        # Перекладываем элементы, только если выходной стек пуст
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    

