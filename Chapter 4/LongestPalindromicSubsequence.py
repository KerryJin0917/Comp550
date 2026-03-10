def LPS_with_string(A):
    n = len(A)
    # 1. Fill the DP table (same logic as before)
    d = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        d[i][i] = 1
        for j in range(i + 1, n):
            if A[i] == A[j]:
                d[i][j] = d[i + 1][j - 1] + 2
            else:
                d[i][j] = max(d[i + 1][j], d[i][j - 1])

    # 2. Backtrack to find the actual string
    lps_str = [""] * d[0][n - 1]
    i, j = 0, n - 1
    start, end = 0, d[0][n - 1] - 1

    while i <= j:
        if A[i] == A[j]:
            # Match found: place character at both ends of the result
            lps_str[start] = A[i]
            lps_str[end] = A[i]
            i += 1
            j -= 1
            start += 1
            end -= 1
        elif d[i + 1][j] > d[i][j - 1]:
            # Move down (exclude A[i])
            i += 1
        else:
            # Move left (exclude A[j])
            j -= 1

    return d[0][n - 1], "".join(lps_str)

def LPS(A):
    n = len(A)
    d = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        d[i][i] = 1
        for j in range(i + 1, n):
            if A[i] == A[j]:
                d[i][j] = d[i + 1][j - 1] + 2
            else:
                d[i][j] = max(d[i + 1][j], d[i][j - 1])
    return d[0][n - 1]

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    A = "accabbbcaacbcabcaccaabcbabaabbaaabaacbbaccaacccbcc"
    print("LPS: ", LPS(A))