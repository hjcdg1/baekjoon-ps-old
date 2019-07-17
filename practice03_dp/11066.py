# PyPy3로 제출해야 시간초과 안 뜨고 성공함

T = int(input())
K = []
Size = []
for i in range(T) :
    K.append(int(input()))
    input_data = input().split()
    Size.append([0 for _ in range(K[i])])
    for j in range(K[i]) :
        Size[i][j] = int(input_data[j])

def min_cost(k, size) :
    M = [ [[0, 0] for _ in range(k)] for _ in range(k) ]
    for i in range(k) :
        M[i][i][0] = size[i]

    for d in range(1, k) :
        for i in range(k-d) :
            j = i + d

            M[i][j][0] = M[i][i][0] + M[i+1][j][0]

            min_ = float('inf')
            for t in range(i, j) :
                temp = M[i][t][1] + M[t+1][j][1] + M[i][j][0]
                if (temp < min_) :
                    min_ = temp
            M[i][j][1] = min_

    return M[0][k-1][1]

for i in range(T) :
    print(min_cost(K[i], Size[i]))
