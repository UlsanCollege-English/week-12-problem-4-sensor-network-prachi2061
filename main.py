import heapq

def prim_mst(graph, start):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
    - graph: A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    - start: The starting node for the algorithm.
    
    Returns:
    - mst_edges: A list of tuples (u, v, weight) representing the edges in the MST.
    - total_cost: The total weight of the MST.
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not in graph")
    
    visited = set()
    mst_edges = []
    total_cost = 0
    # Priority queue: (weight, node, parent)
    pq = [(0, start, None)]
    
    while pq:
        weight, node, parent = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        total_cost += weight
        
        if parent is not None:
            mst_edges.append((parent, node, weight))
        
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor, node))
    
    # Check if all nodes are visited (graph is connected)
    if len(visited) != len(graph):
        raise ValueError("Graph is not connected")
    
    return mst_edges, total_cost
