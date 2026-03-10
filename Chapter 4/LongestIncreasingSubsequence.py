def LIS(A):
    n = len(A)
    d = [1] * n
    p = [-1] * n # 1. Predecessor array
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                p[i] = j
    # 2. Find where the longest sequence ends
    max_idx = d.index(max(d))
    
    # 3. Backtrack to collect the elements
    path = []
    while max_idx != -1:
        path.append(A[max_idx])
        max_idx = p[max_idx] # Move to the parent
        
    return path[::-1]

def LIS_length(A):
    n = len(A)
    d = [1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    A = [14, 84, 76, 26, 50, 45, 65, 79, 10, 3, 83, 43, 76, 1, 45, 72, 23, 94, 90, 4, 3, 54, 93, 38, 22, 42, 3, 22, 44, 50, 24, 23, 22, 46, 29, 3, 83, 56, 64, 19, 99, 86, 12, 33, 72, 71, 93, 42, 83, 67, 31, 59, 88, 84, 51, 59, 4, 25, 79, 42, 18, 55, 70, 67, 38, 44, 51, 78, 52, 39, 49, 3, 5, 70, 98, 59, 39, 17, 50, 98, 77, 54, 86, 23, 51, 95, 58, 46, 27, 55, 95, 1, 78, 82, 88, 74, 81, 52, 56, 43]
    print("Final value of d:", LIS(A))