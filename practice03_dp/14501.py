N = int(input())
T = [ 0 ]
P = [ 0 ]
for i in range(N) :
    input_data = input().split()
    T.append(int(input_data[0]))
    P.append(int(input_data[1]))

def max_profit(N, T, P) :
    D = [0 for _ in range(N+1)]
    D[0] = 0

    M = [[] for _ in range(N+1)]
    for i in range(1, N+1) :
        d = i + T[i] - 1
        if (d <= N) :
            M[d].append(i)

    for i in range(1, N+1) :
        max_ = 0
        while (len(M[i]) != 0) :
            d = M[i].pop()
            if (P[d] + D[d-1] > max_) :
                max_ = P[d] + D[d-1]
        D[i] = max(max_, D[i-1])

    return D[N]

print(max_profit(N, T, P))