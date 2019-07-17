N = int(input())

def stair_number(n) :
    D = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n) ]
    D[0][0] = 0
    for i in range(1, 10) :
        D[0][i] = 1

    for i in range(1, n) :
        D[i][0] = D[i-1][1]
        D[i][9] = D[i-1][8]
        for j in range(1, 9) :
            D[i][j] = D[i-1][j-1] + D[i-1][j+1]

    sum = 0
    for i in range(10) :
        sum += D[n-1][i]

    return sum

print(stair_number(N) % 1000000000)