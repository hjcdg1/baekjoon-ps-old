T = int(input())
N = [0 for _ in range(T)]
M = [0 for _ in range(T)]
for i in range(T) :
    input_data = input().split()
    N[i] = int(input_data[0])
    M[i] = int(input_data[1])

def bridge_case(N, M) :
    C = [ [0] * (M+1) for _ in range(M+1) ]
    C[0][0] = 1
    for i in range(1, M+1) :
        C[i][0] = 1
        C[i][i] = 1
        for j in range(1, i) :
            C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[M][N]

for i in range(T) :
    print(bridge_case(N[i], M[i]))