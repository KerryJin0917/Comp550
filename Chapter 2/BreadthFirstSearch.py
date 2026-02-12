from collections import deque
import math

def bfs(graph, start):
    """
    Perform BFS and compute distance array d.
    graph: adjacency list (1-indexed conceptually, but list indices are 0-based)
    start: starting vertex number (1-indexed)
    Returns list of distances where d[i] = distance from start to vertex i+1
    """
    n = len(graph)
    d = [math.inf] * n
    queue = deque([start])
    d[start - 1] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u - 1]:
            if d[v - 1] == math.inf:
                d[v - 1] = d[u - 1] + 1
                queue.append(v)
    return d


if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    G = [[2, 4], [], [1, 2], [3], []]
    d = bfs(G, 1)
    print("Final values of d:", d)
    print("Final values of d[1:3]:", d[0:3])
    print()

    # Example 2
    print("Example 2:")
    G = [[42], [17, 22, 28, 33], [43, 54], [8, 12, 31, 42, 57], [30, 39, 48, 55, 56, 60], [11, 46], [12], [9, 24, 29, 37, 45], [10, 23, 25, 50, 55], [], [10, 24, 52], [13, 50], [12, 23, 51, 56], [26, 30, 38, 47], [28, 50, 57], [5, 8, 37, 47, 51, 56], [2, 7, 36, 46, 49], [3, 50], [], [17, 42, 59], [18, 28, 53], [5, 12, 33, 36, 41], [35, 56], [27, 47, 55], [7, 10, 33], [1, 9, 28, 47, 56, 58], [3, 32, 40], [26, 31, 34, 56], [23, 33], [22], [25, 29, 43], [33, 46], [4, 26, 59], [1, 10, 11, 14, 26, 32, 53], [24, 55], [30, 48, 55, 59], [1, 45], [35], [16, 18, 40, 49, 50, 57], [5, 57], [7, 17], [14, 19, 47, 51], [29, 44, 58], [45], [9, 23, 56], [27, 34, 47], [7, 25], [1, 2, 5, 7, 51], [25, 43, 54], [1, 32], [4, 41], [20, 41], [33], [3, 9, 22], [3, 21], [48], [17, 19, 20, 42, 45], [29, 33, 53, 54, 57], [11, 27, 48, 53, 58], [4, 25, 26, 34, 57]]
    d = bfs(G, 1)
    print("Final values of d:", d)
    print("Final values of d:", d[0:10])
