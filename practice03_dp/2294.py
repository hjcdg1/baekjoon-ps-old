input_data = input().split()
n = int(input_data[0])
k = int(input_data[1])
v = []
for i in range(n) :
    v.append(int(input()))

def min_coin(n, k, v) :
    M = [0 for _ in range(k+1)]

    M[0] = 0
    M[1] = 1 if 1 in v else -1

    for i in range(2, k+1) :
        min_ = float('inf')
        for j in range(n) :
            if (v[j] <= i and M[i-v[j]] >= 0) :
                if (M[i-v[j]] + 1 < min_) :
                    min_ = M[i-v[j]] + 1
            if (min_ == float('inf')) :
                M[i] = -1
            else :
                M[i] = min_

    return M[k]

print(min_coin(n, k, v))