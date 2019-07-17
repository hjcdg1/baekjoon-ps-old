import sys

N = int(sys.stdin.readline())
seq = sys.stdin.readline().split()
for i in range(N) :
    seq[i] = int(seq[i])

def bitonic(N, seq) :
    # D[i][0] : i번째 글자가 끝인 첫 번째 타입의 가장 긴 바이토닉 수열의 길이
    # D[i][1] : i번째 글자가 끝인 첫 번째 타입의 가장 긴 바이토닉 수열의 길이
    # D[i][2] : i번째 글자가 끝인 첫 번째 타입의 가장 긴 바이토닉 수열의 길이
    # D[i][3] : i번째 글자가 끝인 첫 번째 타입의 가장 긴 바이토닉 수열
    # D[i][4] : i번째 글자가 끝인 첫 번째 타입의 가장 긴 바이토닉 수열
    # D[i][5] : i번째 글자가 끝인 첫 번째 타입의 가장 긴 바이토닉 수열

    D = [ [-1, -1, -1, '&', '&', '&'] for _ in range(N)]
    D[0][0] = 1
    D[0][1] = 1
    D[0][2] = 1
    D[0][3] = str(seq[0])
    D[0][4] = str(seq[0])
    D[0][5] = str(seq[0])

    for i in range(1, N) :
        max_0 = 1
        max_1 = 1
        max_2 = 1
        D[i][3] = str(seq[i])
        D[i][4] = str(seq[i])
        D[i][5] = str(seq[i])
        for j in reversed(range(i)) :
            if (seq[j] > seq[i]) :
                if (D[j][0] + 1 > max_0) :
                    max_0 = D[j][0] + 1
                    try :
                        D[i][3] = D[j][3] + str(seq[i])
                    except :
                        print(D[j][3])
                        exit()
                if (D[j][1] + 1 > max_0) :
                    max_0 = D[j][1] + 1
                    D[i][3] = D[j][4] + str(seq[i])
                if (D[j][2] + 1 > max_2) :
                    max_2 = D[j][2] + 1
                    D[i][5] = D[j][5] + str(seq[i])

            elif (seq[j] < seq[i]) :
                if (D[j][1] + 1 > max_1) :
                    max_1 = D[j][1] + 1
                    D[i][4] = D[j][4] + str(seq[i])
        D[i][0] = max_0
        D[i][1] = max_1
        D[i][2] = max_2

    ''' For Debugging

    for i in range(N) :
        print("<"+str(i)+"번째>")
        print(D[i][3], end=" ")
        print(D[i][4], end=" ")
        print(D[i][5], end=" ")
        print()
    '''

    max_ = float('-inf')
    for i in range(N) :
        if (D[i][0] > max_) :
            max_ = D[i][0]
        if (D[i][1] > max_) :
            max_ = D[i][1]
        if (D[i][2] > max_) :
            max_ = D[i][2]
    return max_

print(bitonic(N, seq))