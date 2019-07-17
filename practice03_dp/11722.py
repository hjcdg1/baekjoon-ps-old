N = int(input())
seq = input().split()
for i in range(N) :
    seq[i] = int(seq[i])

def LDS(n, seq) :
    D = [0 for _ in range(n)]
    D[0] = 1
    for i in range(1, n) :
        max_ = 0
        for j in range(i) :
            if (seq[j] > seq[i] and D[j] > max_) :
                max_ = D[j]
        D[i] = max_ + 1
    max_ = -1
    for i in range(n) :
        if (D[i] > max_) :
            max_ = D[i]
    return max_

print(LDS(N, seq))