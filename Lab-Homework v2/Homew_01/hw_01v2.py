import csv
import time


def load_routes(filename: str) -> dict:
    """Загружает CSV в словарь (хеш-таблицу) маршрутов."""
    routes = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                stops_list = [s.strip() for s in row['stops'].split(',')]
                routes[int(row['route_id'])] = {
                    "name": row['route_name'],
                    "stops": stops_list
                }
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
    return routes

def build_stop_index(routes: dict) -> dict:
    """Создает индекс: остановка -> список ID маршрутов."""
    stop_index = {}
    for route_id, data in routes.items():
        for stop in data['stops']:
            if stop not in stop_index:
                stop_index[stop] = []
            stop_index[stop].append(route_id)
    return stop_index

def find_routes_by_stop(stop_index: dict, stop_name: str) -> list:
    """Поиск маршрутов за O(1)."""
    return stop_index.get(stop_name, [])
# Бенчмарк
def run_benchmark(stop_index, test_stop="Алматы"):
    """Измеряет скорость 10,000 запросов поиска."""
    print(f"\n--- Бенчмарк: 10,000 запросов для '{test_stop}' ---")
    start_time = time.perf_counter()
    
    for _ in range(10000):
        _ = find_routes_by_stop(stop_index, test_stop)
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Общее время: {duration:.4f} секунд")
    print(f"Среднее время на 1 запрос: {duration/10000:.8f} секунд")
    
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
    
# 1. Загрузка данных
routes = load_routes('routes.csv')

# 2. Поиск по ID
route_1 = routes.get(1)
print(f"Маршрут 1: {route_1['name'] if route_1 else 'Не найден'}")

# 3. Создание индекса остановок
stop_index = build_stop_index(routes)

# 4. Поиск маршрутов через конкретную остановку
found = find_routes_by_stop(stop_index, "Алматы")
print(f"Маршруты через Алматы (ID): {found}")

# 5. Запуск теста производительности
run_benchmark(stop_index, "Алматы")
    

