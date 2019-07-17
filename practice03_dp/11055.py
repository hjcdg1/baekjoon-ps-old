import sys

N = int(sys.stdin.readline())
seq = sys.stdin.readline().split()
for i in range(N) :
    seq[i] = int(seq[i])

def max_sum(N, seq) :
    D = [0 for _ in range(N)]
    D[0] = seq[0]

    for i in range(1, N) :
        max_ = seq[i]
        for j in range(i) :
            if (seq[j] < seq[i] and D[j] + seq[i] > max_) :
                max_ = D[j] + seq[i]
            D[i] = max_

    max_ = float('-inf')
    for i in range(N) :
        if (D[i] > max_) :
            max_ = D[i]

    return max_

print(max_sum(N, seq))