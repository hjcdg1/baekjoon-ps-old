T = int(input())
N = [ int(input()) for _ in range(T) ]

def P(N) :
    D = [ 0 for _ in range(N+5) ]
    D[1] = 1
    D[2] = 1
    D[3] = 1
    D[4] = 2
    D[5] = 2
    for i in range(6, N+1) :
        D[i] = D[i-1] + D[i-5]
    return D[N]

for i in range(T) :
    print(P(N[i]))
