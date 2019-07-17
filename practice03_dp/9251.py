import sys

str1 = sys.stdin.readline()
str2 = sys.stdin.readline()

def LCS(str1, str2) :
    N = len(str1) - 1
    M = len(str2) - 1

    D = [[0] * (M+1) for _ in range(N+1)]

    for i in range(1, N+1) :
        for j in range(1, M+1) :
            if (str1[i-1] == str2[j-1]) :
                D[i][j] = D[i-1][j-1] + 1
            else :
                D[i][j] = max(D[i-1][j], D[i][j-1])

    return D[N][M]

print(LCS(str1, str2))
