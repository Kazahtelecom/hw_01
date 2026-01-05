def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)

    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s 
    """
    reverse_string("hello") → "olleh"
    reverse_string("Алматы") → "ытамлА"
    """
    # Используйте стек: push все символы, затем pop

    pass
class QueueFromStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, item):

        self.stack_in.append(item)
    
    def dequeue(self):
        # Если stack_out пуст, перекладываем из stack_in
        if not self.stack_in and not self.stack_out:
            return None  # Очередь пуста
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    
