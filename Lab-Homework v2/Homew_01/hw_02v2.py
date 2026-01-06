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
    