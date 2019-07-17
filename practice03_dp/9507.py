import sys

t = int(sys.stdin.readline())
n = []
max_ = float('-inf')
for _ in range(t) :
    data = int(sys.stdin.readline())
    n.append(data)
    if (data > max_) :
        max_ = data
D = [0 for _ in range(max_+1)]

def koong(n, D) :
    if (n < 2) :
        return 1
    elif (n == 2) :
        return 2
    elif (n == 3) :
        return 4
    elif (D[n] != 0) :
        return D[n]
    else :
        D[0] = 1
        D[1] = 1
        D[2] = 2
        D[3] = 4
        for i in range(4, n+1) :
            D[i] = D[i-1] + D[i-2] + D[i-3] + D[i-4]
        return D[n]

for i in range(t) :
    print(koong(n[i], D))