from math import inf

def dijkstra(G, s_node):
    n = len(G)
    
    # 1. Initialize distances and the empty set S
    # Assuming s_node is 1-indexed based on our previous conversation
    s_idx = s_node - 1
    d = [inf] * n
    d[s_idx] = 0
    S = set()
    
    # 2. While we haven't visited all nodes
    while len(S) < n:
        # u = vertex in V \ S that minimizes d[u]
        u = -1
        min_dist = inf
        
        for i in range(n):
            if i not in S and d[i] < min_dist:
                min_dist = d[i]
                u = i
        
        # If u is still -1, remaining nodes are unreachable
        if u == -1:
            break
            
        # Add u to S
        S.add(u)
        
        # 3. Relax edges: for v in G[u]
        # Your input G[u] = [[v, weight], ...]
        for v_node, weight in G[u]:
            v_idx = v_node - 1 # Convert 1-based to 0-based
            
            # Check if current path is shorter
            if d[u] + weight < d[v_idx]:
                d[v_idx] = d[u] + weight
                
    return d

# --- Example Usage ---
G = [[[2, 58], [27, 96]], [[3, 64], [7, 51], [9, 91], [16, 82], [17, 77], [19, 62]], [[4, 93], [23, 85], [26, 86], [28, 92], [30, 50]], [[3, 97], [5, 82]], [[6, 50], [15, 92]], [[7, 95], [11, 90], [22, 53], [26, 97]], [[4, 79], [8, 99], [27, 58]], [[2, 72], [3, 93], [9, 52], [12, 63], [20, 99], [21, 81]], [[10, 86]], [[1, 84], [2, 68], [11, 68]], [[8, 52], [12, 87]], [[5, 61], [13, 88], [17, 52], [23, 94]], [[12, 86], [14, 51]], [[8, 91], [15, 73], [28, 86]], [[2, 96], [12, 66], [16, 55], [17, 58], [18, 89], [23, 74], [24, 77], [26, 78], [28, 63]], [[17, 67]], [[2, 51], [6, 98], [18, 95]], [[4, 79], [7, 95], [8, 69], [16, 71], [19, 87], [20, 94]], [[1, 67], [20, 72]], [[5, 92], [21, 71], [30, 98]], [[8, 59], [22, 56], [25, 61]], [[14, 65], [23, 63], [24, 52]], [[19, 99], [24, 90]], [[11, 72], [16, 54], [22, 59], [25, 63]], [[3, 52], [26, 65], [29, 82]], [[1, 87], [11, 68], [27, 83]], [[1, 70], [21, 91], [28, 51]], [[2, 61], [4, 89], [29, 77]], [[2, 62], [6, 66], [18, 50], [27, 84], [30, 85]], [[3, 83], [11, 60]]]
s = 1

results = dijkstra(G, s)
print(f"Shortest distances using Dijkstra: {results}")