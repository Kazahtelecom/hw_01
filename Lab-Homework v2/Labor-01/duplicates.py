import time

def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

def find_duplicates_slow(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

# Запуск эксперимента аналогично твоим предыдущим тестам