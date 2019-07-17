input_data = input().split()
N = int(input_data[0])
M = int(input_data[1])
A = [ [0] * (M+1) for _ in range(N+1) ]
D = [ [0] * (M+1) for _ in range(N+1) ]

for i in range(1, N+1) :
    input_data = input().split()
    for j in range(1, M+1) :
        A[i][j] = int(input_data[j-1])

K = int(input())
i = [0] * K
j = [0] * K
x = [0] * K
y = [0] * K
for k in range(K) :
    input_data = input().split()
    i[k] = int(input_data[0])
    j[k] = int(input_data[1])
    x[k] = int(input_data[2])
    y[k] = int(input_data[3])

for p in range(N+1) :
    D[p][0] = 0
for q in range(M+1) :
    D[0][q] = 0

for p in range(1, N+1) :
    for q in range(1, M+1) :
        D[p][q] = D[p-1][q] + D[p][q-1] - D[p-1][q-1] + A[p][q]

for k in range(K) :
    print(D[x[k]][y[k]] - D[i[k]-1][y[k]] - D[x[k]][j[k]-1] + D[i[k]-1][j[k]-1])