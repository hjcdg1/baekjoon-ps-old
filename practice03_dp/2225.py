input_data = input().split()
N = int(input_data[0])
K = int(input_data[1])

def case(N, K) :
    D = [ [0] * (K+1) for _ in range(N+1)]

    # D[i][j] : i를 j개의 숫자로 만드는 경우의 수
    # D[i][j] : 0 ~ i 중의 한 숫자 k를 선택 => (i-k)를 (j-1)개의 숫자로 만드는 경우의 수

    for j in range(K+1) :
        D[0][j] = 1
    for i in range(1, N+1) :
        D[i][0] = 0

    for i in range(1, N+1) :
        for j in range(1, K+1) :
            for k in range(i+1) :
                D[i][j] += D[i-k][j-1]

    return D[N][K]

print(case(N, K) % 1000000000)