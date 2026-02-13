import csv
from graph import Graph


def load_graph(filename):
    """Загрузить CSV → Graph."""
    g = Graph()

    routes = {}

    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            route = row['route']
            order = int(row['order'])
            stop = row['stop']

            routes.setdefault(route, []).append((order, stop))

    # создаём рёбра
    for route, stops in routes.items():
        stops.sort()

        for i in range(len(stops) - 1):
            stop1 = stops[i][1]
            stop2 = stops[i+1][1]

            g.add_edge(stop1, stop2)

    return g


def main():

    print("=== Загрузка графа ===")

    g = load_graph('astana_stops.csv')

    print(f"|V| = {len(g.vertices())}")
    print(f"|E| = {g.edge_count()}")

    print("\n=== Лемма о рукопожатиях ===")

    total_deg = sum(g.degree(v) for v in g.vertices())

    print(f"∑ deg(v) = {total_deg}")
    print(f"2 × |E| = {2 * g.edge_count()}")

    assert total_deg == 2 * g.edge_count()

    print("✓ Лемма подтверждена")

    print("\n=== Топ-3 остановки ===")

    top = sorted(g.vertices(), key=g.degree, reverse=True)[:3]

    for stop in top:
        print(f"{stop}: deg = {g.degree(stop)}")


if __name__ == "__main__":
    main()
