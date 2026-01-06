import csv
import time

def load_routes(filename: str) -> dict:
    """Возвращает {route_id: {"name": str, "stops": list}}"""
    routes = {}
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stops = [s.strip() for s in row['stops'].split(',')]
            routes[int(row['route_id'])] = {"name": row['route_name'], "stops": stops}
    return routes

def find_route(routes: dict, route_id: int) -> dict | None:
    return routes.get(route_id)

def build_stop_index(routes: dict) -> dict:
    stop_index = {}
    for r_id, data in routes.items():
        for stop in data['stops']:
            if stop not in stop_index:
                stop_index[stop] = []
            stop_index[stop].append(r_id)
    return stop_index

def find_routes_by_stop(stop_index: dict, stop_name: str) -> list:
    return stop_index.get(stop_name, [])

# Задача 2.4: Бенчмарк
if __name__ == "__main__":
    routes = load_routes('routes.csv')
    index = build_stop_index(routes)
    start = time.perf_counter()
    for _ in range(10000):
        find_routes_by_stop(index, "Алматы")
    print(f"Benchmark (10,000 requests): {time.perf_counter() - start:.6f} sec")