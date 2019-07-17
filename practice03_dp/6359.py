import sys

T = int(sys.stdin.readline())
n = []
for i in range(T) :
    n.append(int(sys.stdin.readline()))

def DP(n) :
    D = [[0] * (n+1) for _ in range(n+1)]
    # 0 : 잠겨 있음
    # 1 : 열려 있음

    for i in range(n+1) :
        D[0][i] = 0

    for k in range(1, n+1) :
        for i in range(1, n+1) :
            if (i % k == 0) :
                if (D[k-1][i] == 1) :
                    D[k][i] = 0
                elif (D[k-1][i] == 0) :
                    D[k][i] = 1
            else :
                D[k][i] = D[k-1][i]

    num = 0
    for i in range(1, n+1) :
        num += D[n][i]

    return num

for i in range(T) :
    print(DP(n[i]))