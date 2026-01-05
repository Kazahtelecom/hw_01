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