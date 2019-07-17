input_data = input().split()
N = int(input_data[0])
M = int(input_data[1])

def chocolate_case(N, M) :
    D = [ [0] * (M+1) for _ in range(N+1) ]
    for i in range(N+1) :
        D[i][0] = 0
    for j in range(M+1) :
        D[0][j] = 0

    for i in range(1, N+1) :
        for j in range(1, M+1) :
            min_ = float('inf')
            for k in range(1, i) :
                if (D[k][j] + D[i-k][j] + 1 < min_) :
                    min_ = D[k][j] + D[i-k][j] + 1
            for k in range(1, j) :
                if (D[i][k] + D[i][j-k] + 1 < min_) :
                    min_ = D[i][k] + D[i][j-k] + 1
            D[i][j] = min_
            if (i == 1 and j == 1) :
                D[i][j] = 0
    return D[N][M]

print(chocolate_case(N, M))