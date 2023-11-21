class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex):
        self.edges[vertex] = True

    def get_edges(self):
        return list(self.edges.keys())
    
    # def _repr__(self):
    #     return str(self.value) + " Edges: " + str([x.value for x in self.edges])
    
    # def _str_(self):
    #     return str(self.value)
