input_data = input().split()
N = int(input_data[0])
K = int(input_data[1])

def combination(N, K) :
    C = [ [0] * (N+1) for _ in range(N+1) ]
    C[0][0] = 1

    for i in range(1, N+1) :
        C[i][0] = 1
        C[i][i] = 1
        for j in range(1, i) :
            C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[N][K]

print(combination(N, K) % 10007)