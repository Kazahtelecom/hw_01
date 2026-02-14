import csv
from graph import Graph
from traversals import bfs, dfs, shortest_path
from components import find_components


def load_graph(filename):

    g = Graph()
    routes = {}

    with open(filename, encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:

            route = row['route']
            order = int(row['order'])
            stop = row['stop']

            routes.setdefault(route, []).append((order, stop))

    for route, stops in routes.items():

        stops.sort()

        for i in range(len(stops)-1):

            g.add_edge(stops[i][1], stops[i+1][1])

    return g


def main():

    g = load_graph('astana_stops.csv')

    print("\n=== ЧАСТЬ B1: BFS ===")

    order = bfs(g, 'Микрорайон Самал')

    print(f'Посещено: {len(order)} из {len(g.vertices())}')
    print("Первые 5:", order[:10])


    print("\n=== ЧАСТЬ B2: DFS ===")

    order_dfs = dfs(g, 'Микрорайон Самал')

    print(f'Посещено: {len(order_dfs)} из {len(g.vertices())}')
    print("Первые 5:", order_dfs[:10])


    print("\n=== ЧАСТЬ B3: shortest_path ===")

    path = shortest_path(
        g,
        'ТЖ Вокзал',
        'ЕНУ им. Гумилёва'
    )

    if path:

        print(f'Путь ({len(path)-1} остановок):')
        print(" → ".join(path))

    else:
        print("Путь не найден")


    print("\n=== ЧАСТЬ C1: components ===")

    comps = find_components(g)

    print(f'Компонент: {len(comps)}')

    for i, comp in enumerate(comps):

        print(f'Компонента {i+1}: {len(comp)} вершин')


    print("\n=== ЧАСТЬ C2: удаление хаба ===")

    g2 = Graph()

    for v in g.vertices():

        if v == 'Микрорайон Самал':
            continue

        for u in g.neighbors(v):

            if u != 'Микрорайон Самал':
                g2.add_edge(v, u)

    comps2 = find_components(g2)

    print(f'Без Самал: {len(comps2)} компонент')


if __name__ == "__main__":
    main()
