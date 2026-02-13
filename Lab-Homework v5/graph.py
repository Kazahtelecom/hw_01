from collections import defaultdict

class Graph:
    """Граф на списке смежности."""
    
    def __init__(self):
        self.adj = defaultdict(set)  # set, чтобы не было дублей
    
    def add_edge(self, u, v):
        """Добавить ребро u—v (неориентированный)."""
        # Ваш код: добавьте v в adj[u] и u в adj[v]
        self.adj[u].add(v)
        self.adj[v].add(u)

        
    
    def neighbors(self, v):
        """Вернуть множество соседей вершины v."""
        return self.adj[v]
    
    def vertices(self):
        """Вернуть множество всех вершин."""
        return set(self.adj.keys())
    
    def degree(self, v):
        """Степень вершины: deg(v) = число соседей."""
        return len(self.adj[v])
        
    
    def edge_count(self):
        """Число рёбер |E|. Подсказка: ∑ deg(v) = 2|E|."""
        total_degree = sum(self.degree(v) for v in self.vertices())
        return total_degree // 2  # делим на 2, так как каждое ребро посчитано дважды
        
        