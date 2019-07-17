N = int(input())
input_list = [ -1 ]
for _ in range(N) :
    input_list.append(int(input()))

def MaxStairPoint(N, points) :
    # M[n] : n-1번째 계단을 거치지 않고 n번째 계단에 도착하는 경우의 최대 점수
    # M[n] : n-1번째 계단을 거치고 n번째 계단에 도착하는 경우의 최대 점수
    M = [ [0, 0] for _ in range(N + 1) ]

    M[0][0] = 0
    M[0][1] = 0
    M[1][0] = points[1]
    M[1][1] = points[1]

    for i in range(2, N + 1) :
        M[i][0] = max(M[i - 2][0], M[i - 2][1]) + points[i]
        M[i][1] = M[i - 1][0] + points[i]

    return max(M[N][0], M[N][1])

print(MaxStairPoint(N, input_list))