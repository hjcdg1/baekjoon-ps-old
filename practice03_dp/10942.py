import sys

N = int(sys.stdin.readline())
seq = sys.stdin.readline().split()
for i in range(N) :
    seq[i] = int(seq[i])
M = int(sys.stdin.readline())
S = [0 for _ in range(M)]
E = [0 for _ in range(M)]
for i in range(M) :
    input_data = sys.stdin.readline().split()
    S[i] = int(input_data[0])
    E[i] = int(input_data[1])

def palindrome(seq, D) :
    for i in range(N) :
        D[i][i] = 1
    for i in range(N-1) :
        D[i][i+1] = 1 if seq[i] == seq[i+1] else 0

    for d in range(2, N) :
        for start in range(N-d) :
            end = start + d
            if (seq[start] == seq[end] and D[start+1][end-1] == 1) :
                D[start][end] = 1

D = [[0] * N for _ in range(N)]
palindrome(seq, D)
for i in range(M) :
    print(D[S[i]-1][E[i]-1])
