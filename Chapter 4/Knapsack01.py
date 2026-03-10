def KnapsackDP(v, w, B):
    n = len(v)
    d = [[0] * (B + 1) for _ in range(n + 1)]
    for j in range(B + 1):
        if j >= w[0]:
            d[1][j] = v[0]
    for i in range(1, n + 1):
        for j in range(B + 1):
            if w[i - 1] <= j:
                d[i][j] = max(d[i - 1][j], d[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                d[i][j] = d[i - 1][j]
    return d[n][B]

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    v = [3, 17, 15, 5, 10, 9, 13, 15, 2, 1, 16, 9, 15, 1, 9, 14, 5, 18, 18, 1, 1, 11, 18, 8, 5, 9, 1, 5, 9, 10, 5, 5, 5, 9, 6, 1, 16, 11, 13, 4, 19, 17, 3, 7, 14, 14, 18, 9, 16, 13]
    w = [6, 12, 17, 17, 10, 12, 1, 5, 16, 8, 4, 11, 14, 13, 8, 9, 10, 15, 10, 8, 10, 1, 1, 14, 19, 12, 8, 4, 10, 19, 15, 11, 17, 5, 10, 19, 11, 9, 6, 11, 19, 1, 15, 16, 17, 15, 16, 10, 11, 9]
    B = 40
    print("Knapsack DP: ", KnapsackDP(v, w, B))