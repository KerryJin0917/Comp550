from math import inf
from collections import deque

def dag_shortest_path(G, s_node):
    n = len(G)
    # We create a distance array of size n+1 to allow 1-based indexing
    # so that d[2] is the distance to Node 2.
    d = [inf] * (n + 1)
    d[s_node] = 0
    
    # Standard 0-indexed topo sort for the list G
    topo_order_indices = get_topological_sort(G)
    
    # Process nodes in topological order
    for u_idx in topo_order_indices:
        u_node = u_idx + 1 # Convert 0-index back to 1-based node label
        
        # Look at neighbors of the current node
        for v_node, weight in G[u_idx]:
            if d[u_node] + weight < d[v_node]:
                d[v_node] = d[u_node] + weight
                
    return d

def get_topological_sort(G):
    n = len(G)
    in_degree = [0] * n
    for u in range(n):
        for v_node, w in G[u]:
            v_idx = v_node - 1
            in_degree[v_idx] += 1
            
    queue = deque([i for i, degree in enumerate(in_degree) if degree == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v_node, w in G[u]:
            v_idx = v_node - 1
            in_degree[v_idx] -= 1
            if in_degree[v_idx] == 0:
                queue.append(v_idx)
    return topo_order

# Your input
G = [[[2, 3], [3, 5], [4, 6]], [[3, 4]], [[4, -1]], []]
s = 1 # Starting at Node 1

distances = dag_shortest_path(G, s)

# Now distances[2] will be 3
print(f"The distance to Node 2 (d[2]) is: {distances[2]}")
print(f"Full distance array (1-indexed): {distances[1:]}")