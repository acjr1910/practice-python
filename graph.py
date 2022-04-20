class Graph():
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1] = list(filter(
                lambda v: (v != vertex2), self.adjacency_list[vertex1]))
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex2] = list(filter(
                lambda v: (v != vertex1), self.adjacency_list[vertex2]))

    def remove_vertex(self, vertex):
        for v in self.adjacency_list:
            self.remove_edge(vertex, v)
        del self.adjacency_list[vertex]


graph = Graph()

graph.add_vertex('porto')
graph.add_vertex('tokyo')
graph.add_vertex('porto')  # checks collision
graph.add_vertex('aspen')
graph.add_vertex('berlim')

graph.add_edge('porto', 'tokyo')
graph.add_edge('porto', 'aspen')
graph.add_edge('porto', 'berlim')

graph.add_edge('tokyo', 'berlim')
graph.add_edge('tokyo', 'aspen')

print(graph.adjacency_list)

graph.remove_vertex('porto')
print(graph.adjacency_list)
