import sys

str1 = sys.stdin.readline()
str2 = sys.stdin.readline()

def LCS(str1, str2) :
    N = len(str1) - 1
    M = len(str2) - 1

    D = [[[0, 0] for _ in range(M+1)] for _ in range(N+1)]
    # 1 : 왼쪽에서 옴
    # 2 : 위쪽에서 옴
    # 3 : 대각선에서 옴

    for i in range(1, N+1) :
        for j in range(1, M+1) :
            if (str1[i-1] == str2[j-1]) :
                D[i][j][0] = D[i-1][j-1][0] + 1
                D[i][j][1] = 3
            else :
                if (D[i-1][j][0] >= D[i][j-1][0]) :
                    D[i][j][0] = D[i-1][j][0]
                    D[i][j][1] = 2
                else :
                    D[i][j][0] = D[i][j-1][0]
                    D[i][j][1] = 1

    str_list = []
    i = N
    j = M
    while (i != 0 and j != 0) :
        if (D[i][j][1] == 1) :
            j -= 1
        elif (D[i][j][1] == 2) :
            i -= 1
        elif (D[i][j][1] == 3) :
            str_list.append(str1[i-1])
            i -= 1
            j -= 1

    return (D[N][M][0], "".join(reversed(str_list)))

temp = LCS(str1, str2)
print(temp[0])
print(temp[1])
