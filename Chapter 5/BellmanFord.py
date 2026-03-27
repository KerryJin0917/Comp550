from math import inf

def bellman_ford_dp(G, s_node):
    n = len(G)
    
    # 1. Initialize d[v][j] matrix (size n+1 by n)
    # d[v][j] stores shortest path to node v using at most j edges
    # We use n+1 for rows to accommodate 1-based node labels if needed
    d = [[inf] * n for _ in range(n + 1)]
    
    # Initial condition: distance to source with 0 edges is 0
    d[s_node][0] = 0
    
    # 2. G^R = reverse of G (Predecessor map)
    # Mapping: v -> list of (u, weight)
    reversed_g = [[] for _ in range(n + 1)]
    for u_idx, neighbors in enumerate(G):
        u_node = u_idx + 1 # Converting 0-index to 1-based
        for v_node, weight in neighbors:
            reversed_g[v_node].append((u_node, weight))
            
    # 3. Main Loops
    # j is the number of edges (from 1 to n-1)
    for j in range(1, n):
        for v in range(1, n + 1):
            # Case A: Shortest path to v remains the same as with j-1 edges
            d[v][j] = d[v][j-1]
            
            # Case B: Try to find a shorter path ending with edge (u, v)
            for u, weight in reversed_g[v]:
                if d[u][j-1] != inf:
                    d[v][j] = min(d[v][j], d[u][j-1] + weight)
                    
    # 4. Return the last column (distances for all nodes at j = n-1)
    # We skip index 0 of the result if using 1-based indexing
    final_distances = [row[n-1] for row in d]
    return final_distances[1:]

# --- Example Usage ---
G = [[[2, 53], [6, -66], [14, -84], [15, -52], [16, 70], [17, 83], [27, 76], [29, -87]], [[3, 78], [10, -72], [13, 96], [14, -81], [16, -60], [17, -99], [18, 95], [19, -82], [25, -54], [29, -56]], [[4, 91], [8, -58], [9, 63], [10, 95], [19, 58], [20, 61], [26, 89]], [[5, 69], [9, -89], [17, 87], [21, 66]], [[6, 90], [8, -52], [9, 78]], [[7, 84], [10, -96], [11, 51], [18, 83], [19, 73], [21, 51], [22, 56], [24, -51], [25, 90]], [[8, 73], [18, 57], [20, -63]], [[9, 83], [10, -96], [11, -93], [18, -86], [21, 76], [22, -93], [23, -58], [24, 95]], [[10, 98], [17, 72], [24, 82]], [[11, 73], [12, 97], [13, 96], [18, -50], [21, 61], [22, 63], [25, -56], [28, 87]], [[12, 89], [20, 50], [21, -92]], [[13, 98], [16, -66], [19, 60], [21, -59], [24, 84], [25, -63], [26, 91]], [[14, 66], [15, 91], [16, 91], [18, 90], [21, 82], [28, 74], [29, 72]], [[15, 79], [18, 58], [19, 90], [23, 98], [29, -75], [30, -67]], [[16, 96], [17, -94], [24, -84], [30, 80]], [[17, 55], [18, 74], [23, -98], [27, -84]], [[18, 70], [21, -71]], [[19, 99], [21, 54], [26, 99], [28, 53]], [[20, 89], [21, -89], [25, -94]], [[21, 87], [23, -61]], [[22, 59], [24, 91], [26, 54]], [[23, 53], [27, 83], [28, 81]], [[24, 65]], [[25, 75], [26, -82], [30, 63]], [[26, 61]], [[27, 75]], [[28, 56]], [[29, 98]], [[30, 67]], []]
s = 1

result = bellman_ford_dp(G, s)
print(f"Shortest distances using Bellman-Ford DP: {result}")