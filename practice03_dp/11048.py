input_data = input().split()
N = int(input_data[0])
M = int(input_data[1])
A = [ [0] * (M+1) for _ in range(N+1) ]
for i in range(N) :
    input_data = input().split()
    for j in range(M) :
        A[i+1][j+1] = int(input_data[j])

def max_candy(N, M, A) :
    D = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            D[i+1][j+1] = max(D[i][j], D[i+1][j], D[i][j+1]) + A[i+1][j+1]
    return D[N][M]

print(max_candy(N, M, A))