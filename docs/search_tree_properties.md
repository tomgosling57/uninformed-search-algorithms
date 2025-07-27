# Graph Search Class Properties

## Graph Class

```python
class Graph:
    def __init__(self):
        self.nodes = {}       # Dictionary of nodes (key: node_id, value: GraphNode)
        self.adjacency = {}    # Adjacency list (key: node_id, value: list of neighbors)
    
    # Core Methods
    def add_node(self, node_id): pass  # Add new node
    def add_edge(self, node1, node2): pass  # Add undirected edge
    def get_neighbors(self, node_id): pass  # Return adjacent nodes
    
    # Properties
    @property
    def size(self): return len(self.nodes)
    @property
    def is_empty(self): return len(self.nodes) == 0
```

## GraphNode Class

```python
class GraphNode:
    def __init__(self, node_id, data=None):
        self.id = node_id      # Unique node identifier
        self.data = data       # Optional node data
        self.visited = False   # For search algorithms
        
    # Properties
    @property
    def is_visited(self): return self.visited
```

## BFS Integration

1. **Graph Representation**: Graph uses adjacency list for efficient neighbor lookup
2. **BFS Requirements**:
   - `queue` manages nodes to visit
   - `visited` set tracks explored nodes
   - `get_neighbors()` provides adjacent nodes
3. **Implementation Notes**:
   - Reset `visited` flags before each search
   - Node IDs should be hashable for set operations
   - Graph can be directed or undirected based on edge addition