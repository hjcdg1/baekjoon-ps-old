N = int(input())

def increasing_number(N) :
    D = [ [0] * 10 for _ in range(N+1)]
    for i in range(10) :
        D[1][i] = 1

    for i in range(2, N+1) :
        for j in range(10) :
            for k in range(j+1) :
                D[i][j] += D[i-1][k]

    sum = 0
    for i in range(10) :
        sum += D[N][i]
    return sum

print(increasing_number(N) % 10007)