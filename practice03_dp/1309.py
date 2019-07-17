N = int(input())

def cases(N) :
    D = [[0, 0] for _ in range(N)]
    D[0][0] = 1
    D[0][1] = 2
    for i in range(1, N) :
        D[i][0] = (D[i-1][0] + D[i-1][1]) % 9901
        D[i][1] = (2 * D[i-1][0] + D[i-1][1]) % 9901
    return D[N-1][0] + D[N-1][1]

print(cases(N) % 9901)