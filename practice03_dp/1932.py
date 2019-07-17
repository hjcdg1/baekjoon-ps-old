n = int(input())
level = [ [] for _ in range(n) ]
for i in range(n) :
    input_data = input().split()
    for j in range(i+1) :
        level[i].append(int(input_data[j]))

def max_path(n, level) :
    D = [ [0] * (i+1) for i in range(n) ]
    for i in range(n) :
        D[n-1][i] = level[n-1][i]

    for i in reversed(range(n-1)) :
        for j in range(i+1) :
            D[i][j] = max(D[i+1][j], D[i+1][j+1]) + level[i][j]

    return D[0][0]

print(max_path(n, level))

# D[i][j] = max(D[i+1][j], D[i+1][j+1])  (0 <= i <= n-1, 0 <= j <= i+1)
# D[n-1][0] = level[n-1][0]
# D[n-1][1] = level[n-1][1]
# ...
# D[n-1][n-1] = level[n-1][n-1]
