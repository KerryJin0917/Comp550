from collections import deque
import math

def dfs(graph):
    """
    Perform DFS and compute distance array d.
    """
    pre = [math.inf] * len(graph)
    post = [math.inf] * len(graph)
    t = [1]
    def explore(u):
        pre[u] = t[0]
        t[0] += 1
        for v in graph[u]:
            v_idx = v - 1
            if pre[v_idx] == math.inf:
                explore(v_idx)
        post[u] = t[0]
        t[0] += 1
        
    for u in range(len(graph)):
        if pre[u] == math.inf:
            explore(u)
        
    return pre, post

def back_edges(graph, pre, post):
    """
    Identify back edges in the graph using pre and post arrays.
    """
    back_edges_list = 0
    for u in range(len(graph)):
        for v in graph[u]:
            v_idx = v - 1
            if pre[v_idx] < pre[u] and post[v_idx] > post[u]:
                back_edges_list += 1
    return back_edges_list

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    G = [[19, 20, 24], [3, 9, 37], [2, 9, 14], [30], [4, 16, 21, 29, 33], [9, 13, 19, 24, 29, 39], [18, 20, 32, 39], [1, 2, 11, 17, 18, 19, 23, 33, 37], [3, 26, 29, 34, 36, 38], [1, 3, 15], [12, 13, 31, 32], [7, 11, 13, 20, 21, 28, 29], [14, 27, 29], [15, 20, 33], [3, 27], [15, 20, 29, 31], [18, 37, 38], [5, 10, 20, 36, 40], [18, 21, 29], [17, 23, 28], [8, 12, 14, 15, 16, 18, 19, 25, 30, 34, 40], [24, 27, 31, 35], [17, 25, 33, 36], [1, 2, 4, 5, 25, 35, 39], [4, 10, 14, 15, 34, 39], [4, 7, 14, 16, 17, 32], [14, 39], [19, 26], [1, 27], [7, 8, 17, 32, 33], [4, 9, 22, 28, 30, 38], [10, 23, 25, 30, 36, 37], [2, 3, 9, 23, 26, 31], [], [6, 27, 37], [1, 15, 18, 31, 32, 39], [7, 10, 15, 19, 22, 27, 29, 31], [5, 11, 27, 33], [2, 8, 20, 24, 40], [9, 11, 14, 16, 36]]
    d = dfs(G)
    print("Final values of d:", d)
    pre, post = d
    print("pre:", pre[0:10])
    print("post:", post[0:10])
    print(back_edges(G, pre, post))

