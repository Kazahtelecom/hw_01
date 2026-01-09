# Задача 1.1: Реверс строки через стек
def reverse_string(s: str) -> str:
    """Переворачивает строку, используя принцип LIFO."""
    stack = []
    # Push: кладем каждый символ в стек
    for char in s:
        stack.append(char)
    
    reversed_s = ""
    # Pop: достаем с вершины, пока стек не опустеет
    while stack:
        reversed_s += stack.pop()
    return reversed_s

# Задача 1.2: Очередь из двух стеков
class QueueFromStacks:
    def __init__(self):
        self.stack_in = []   # Стек для добавления (enqueue)
        self.stack_out = []  # Стек для удаления (dequeue)
    
    def enqueue(self, item):
        """Добавляет элемент в конец очереди за O(1)."""
        self.stack_in.append(item)
    
    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди."""
        # Если оба стека пусты — очередь пуста
        if not self.stack_in and not self.stack_out:
            return None
            
        # Если выходной стек пуст, перекладываем всё из входного
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
                
        return self.stack_out.pop()

# Тестирование Части 1
if __name__ == "__main__":
    print(f"Реверс 'Алматы': {reverse_string('Алматы')}")
    
    q = QueueFromStacks()
    q.enqueue("A")
    q.enqueue("B")
    print(f"Dequeue 1: {q.dequeue()}") # Ожидаем A
    q.enqueue("C")
    print(f"Dequeue 2: {q.dequeue()}") # Ожидаем B