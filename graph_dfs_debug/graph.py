"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Vertex already exists!')
        if not set(edges).issubset(self.vertices):
            raise Exception("Edges can't exist there!")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices:
            raise Exception("Start not in graph!")
        if end not in self.vertices:
            raise Exception("End not in graph!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set()
        while stack:
            current = stack.pop()
            if current == target:
                break
            stack.extend((self.vertices[current]))
            visited.add(current)
        return visited

    def graph_rec(self, start, target=None):
        queue = set()
        queue.set(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return queue

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
