import sys, math

input_data = sys.stdin.readline().split()
N = int(input_data[0])
M = int(input_data[1])
K = int(input_data[2])

def DP(N, M, K) :
    C = [[0] * (M+N+1) for _ in range(M+N+1)]
    C[0][0] = 1
    for i in range(1, N+M+1) :
        C[i][0] = 1
        C[i][i] = 1
        for j in range(1, i) :
            C[i][j] = C[i-1][j-1] + C[i-1][j]

    if (K == 0) :
        return C[N+M-2][N-1]
    else :
        r = int(math.ceil(K / M))
        c = K % M
        if (c == 0) :
            c = M
        return C[r+c-2][r-1] * C[N+M-r-c][N-r]

print(DP(N, M, K))
