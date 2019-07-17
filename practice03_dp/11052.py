N = int(input())
input_data = input().split()
cost = [-1]
for i in range(N) :
    cost.append(int(input_data[i]))

def maxCost(n, cost) :
    C = [0 for _ in range(n+1)]
    C[1] = cost[1]
    for i in range(2, n+1) :
        max_ = cost[i]
        for j in range(1, i) :
            if (C[i-j] + C[j] > max_) :
                max_ = C[i-j] + C[j]
        C[i] = max_
    return C[n]

print(maxCost(N, cost))