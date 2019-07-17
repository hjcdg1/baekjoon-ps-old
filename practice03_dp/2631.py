# LIS 활용

import sys

n = int(sys.stdin.readline())
seq = []
for _ in range(n) :
    seq.append(int(sys.stdin.readline()))

def LIS(n, seq) :
    D = [0 for _ in range(n)]
    D[0] = 1
    for i in range(1, n) :
        max_ = 0
        for j in range(i) :
            if (seq[j] < seq[i] and D[j] > max_) :
                max_ = D[j]
        D[i] = max_ + 1
    max_ = -1
    for i in range(n) :
        if (D[i] > max_) :
            max_ = D[i]
    return max_

print(n-LIS(n, seq))