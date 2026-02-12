def fractional_knapsack(v, w, B):
    n = len(v)
    items = [(v[i] / w[i], i) for i in range(n)]
    items.sort(key=lambda x: x[0], reverse=True)
    x = [0] * n
    remaining_capacity = B
    
    for ratio, i in items:
        if remaining_capacity <= 0:
            break
        amount = min(w[i], remaining_capacity)
        x[i] = amount / w[i]
        remaining_capacity -= amount
        
    return x

def optimal_value(v, w, B):
    x = fractional_knapsack(v, w, B)
    return sum(x[i] * v[i] for i in range(len(v)))

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    v = [64, 111, 58, 168, 98, 192, 142, 129, 214, 205, 240, 243, 127, 190, 150, 216, 221, 242, 242, 123, 215, 237, 113, 93, 202, 187, 71]
    w = [1, 2, 2, 23, 10, 38, 16, 24, 8, 18, 31, 59, 14, 27, 46, 21, 64, 49, 35, 40, 37, 11, 3, 10, 14, 44, 5]
    B = 31
    print("Final values of d:", fractional_knapsack(v, w, B))
    print("Optimal value:", optimal_value(v, w, B))