class WeightedGraph():
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacency_list[v1].append({'node': v2, 'weight': weight})
        self.adjacency_list[v2].append({'node': v1, 'weight': weight})


graph = WeightedGraph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

graph.add_edge('A', 'B', 9)
graph.add_edge('A', 'C', 5)
graph.add_edge('B', 'C', 7)


print(graph.adjacency_list)
