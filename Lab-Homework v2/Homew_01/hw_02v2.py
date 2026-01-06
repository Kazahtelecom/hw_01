import csv
import time

# --- 0. Создаем тестовый файл routes.csv ---
def create_sample_csv():
    with open('routes.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['route_id', 'route_name', 'stops']) # Заголовки
        writer.writerow(['1', 'Алматы-Астана', 'Алматы, Караганда, Астана'])
        writer.writerow(['2', 'Алматы-Шымкент', 'Алматы, Тараз, Шымкент'])
        writer.writerow(['3', 'Астана-Павлодар', 'Астана, Экибастуз, Павлодар'])

# --- 1. Твои функции загрузки и поиска ---
def load_routes(filename: str) -> dict:
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
        return {}
    return routes

def build_stop_index(routes: dict) -> dict:
    stop_index = {}
    for route_id, data in routes.items():
        for stop in data['stops']:
            if stop not in stop_index:
                stop_index[stop] = []
            stop_index[stop].append(route_id)
    return stop_index

def find_routes_by_stop(stop_index: dict, stop_name: str) -> list:
    return stop_index.get(stop_name, [])

# --- 2. Запуск всего процесса ---
create_sample_csv() # Теперь файл точно существует!

routes = load_routes('routes.csv')
route_1 = routes.get(1)

if route_1:
    print(f"Маршрут 1: {route_1['name']}")
else:
    print("Маршрут 1: Не найден")

stop_index = build_stop_index(routes)
target = "Алматы"
found = find_routes_by_stop(stop_index, target)
print(f"Маршруты через {target} (ID): {found}")

# --- 3. Бенчмарк ---
start_time = time.perf_counter()
for _ in range(10000):
    _ = find_routes_by_stop(stop_index, target)
end_time = time.perf_counter()

print(f"\n--- Бенчмарк: 10,000 запросов ---")
print(f"Общее время: {end_time - start_time:.6f} секунд")
    