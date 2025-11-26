import heapq

def prim_mst(graph, start):
    if start not in graph:
        raise ValueError(f"Start node '{start}' not in graph")

    visited = set()
    mst_edges = []
    total_cost = 0

    # Priority queue: (weight, parent, node) for alphabetical tie-breaking
    pq = [(0, "", start)]

    while pq:
        weight, parent, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if parent != "":
            mst_edges.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                # Sorting ensures consistent MST structure
                p = min(node, neighbor)
                n = max(node, neighbor)
                heapq.heappush(pq, (w, p, n))

    if len(visited) != len(graph):
        raise ValueError("Graph is not connected")

    return mst_edges, total_cost
