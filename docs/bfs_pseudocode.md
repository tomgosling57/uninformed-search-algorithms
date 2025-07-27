# Breadth-First Search (BFS) Pseudocode

```pseudocode
function BFS(graph, start_node_id):
    // Initialize a queue for BFS
    queue = new Queue()
    queue.enqueue(start_node_id)
    
    // Mark starting node as visited
    graph.nodes[start_node_id].visited = True
    
    while queue is not empty:
        current_id = queue.dequeue()
        current_node = graph.nodes[current_id]
        
        // Process current node
        process(current_node)
        
        // Visit all adjacent nodes
        for neighbor_id in graph.get_neighbors(current_id):
            neighbor = graph.nodes[neighbor_id]
            if not neighbor.visited:
                neighbor.visited = True
                queue.enqueue(neighbor_id)
```

## Explanation

1. **Queue Initialization**: BFS uses a queue to track nodes to visit
2. **Visited Tracking**: Prevents revisiting nodes and infinite loops
3. **Processing**: Nodes are processed in FIFO (first-in, first-out) order
4. **Neighbor Exploration**: All unvisited neighbors are added to the queue

## Time Complexity
- O(V + E) where V is vertices and E is edges
- Visits every vertex and edge once