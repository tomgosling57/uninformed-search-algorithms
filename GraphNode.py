class GraphNode:
    def __init__(self, node_id, data=None):
        self.id = node_id      # Unique node identifier
        self.data = data       # Optional node data
        self.visited = False   # For search algorithms
        
    # Properties
    @property
    def is_visited(self): return self.visited