# Pick one of the abstract data structures mentioned in this section that you have not yet implemented
# Build a custom Python class that demonstrates its functionality 
# Compare your solution to: https://github.com/david-legend/python-algorithms/tree/main/data-structures/src

class Graph:

    def __init__(self, graph=None) -> None:
        self.edges = {} if graph is None else graph
    
    def add_edge(self, vertex1, vertex2):
        
        if vertex1 not in self.edges.keys():
            self.edges[vertex1] = []
        if vertex2 not in self.edges.keys():
            self.edges[vertex2] = []

        if vertex1 not in self.edges[vertex2]:
            self.edges[vertex2].append(vertex1)
        if vertex2 not in self.edges[vertex1]:
            self.edges[vertex1].append(vertex2)
        
    def __getitem__(self, vertex):
        return self.edges[vertex]
    
    def __repr__(self) -> str:
        return repr(self.edges)

g = Graph()
g.add_edge("a", "b")
g.add_edge("a", "c")
g.add_edge("b", "c")
g.add_edge("c", "d")

print(g)