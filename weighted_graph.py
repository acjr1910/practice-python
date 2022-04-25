from priority_queue import PriorityQueue


class WeightedGraph():
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacency_list[v1].append({'node': v2, 'weight': weight})
        self.adjacency_list[v2].append({'node': v1, 'weight': weight})

    def dijkstra(self, start, end):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []  # return at the end
        smallest = None

        # build initial distances state
        for vertex in self.adjacency_list:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')  # infinity
                nodes.enqueue(vertex, float('inf'))
            previous[vertex] = None

        while len(nodes.values):
            smallest = nodes.dequeue()['value']
            if smallest == end:
                while(previous[smallest]):
                    path.append(smallest)
                    smallest = previous[smallest]
                break
            if smallest or distances[smallest] != float('inf'):
                for neighbor in range(len(self.adjacency_list[smallest])):
                    next_node = self.adjacency_list[smallest][neighbor]
                    candidate = distances[smallest] + next_node['weight']
                    next_neighbor = next_node['node']
                    if candidate < distances[next_neighbor]:
                        distances[next_neighbor] = candidate
                        previous[next_neighbor] = smallest
                        nodes.enqueue(next_neighbor, candidate)

        path.append(smallest)
        path.reverse()
        return path


graph = WeightedGraph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'E', 3)
graph.add_edge('C', 'D', 2)
graph.add_edge('C', 'F', 4)
graph.add_edge('D', 'E', 3)
graph.add_edge('D', 'F', 1)
graph.add_edge('E', 'F', 1)

print(graph.dijkstra('A', 'E'))
