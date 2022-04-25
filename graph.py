import queue


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

    def depth_first_search(self, vertex):
        edges = []
        visited = {}

        def helper(vertex):
            visited[vertex] = True
            edges.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    helper(neighbor)
        helper(vertex)

        return edges

    def breadth_first_search(self, vertex):
        queue = [vertex]
        edges = []
        visited = {}
        currentVertex = None
        visited[vertex] = True

        while len(queue):
            currentVertex = queue.pop(0)
            edges.append(currentVertex)
            for neighbor in self.adjacency_list[currentVertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return edges


graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')
graph.add_edge('D', 'F')
graph.add_edge('E', 'F')

print('Depth First Search:', graph.depth_first_search("A"))
print('Breadth First Search:', graph.breadth_first_search("A"))
