N = int(input())
cost = [ [0, 0, 0] for _ in range(N + 1) ]
for k in range(1, N + 1) :
    input_data = input().split()
    cost[k][0] = int(input_data[0])
    cost[k][1] = int(input_data[1])
    cost[k][2] = int(input_data[2])

def MinCost(n, cost) :
    C = [ [0, 0, 0] for _ in range(n + 1) ]
    C[1][0] = cost[1][0]
    C[1][1] = cost[1][1]
    C[1][2] = cost[1][2]

    for i in range(2, n + 1) :
        C[i][0] = min(C[i-1][1], C[i-1][2]) + cost[i][0]
        C[i][1] = min(C[i-1][0], C[i-1][2]) + cost[i][1]
        C[i][2] = min(C[i-1][0], C[i-1][1]) + cost[i][2]

    return min(C[n][0], C[n][1], C[n][2])

print(MinCost(N, cost))
