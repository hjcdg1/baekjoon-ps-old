input_data = input().split()
N = int(input_data[0])
M = int(input_data[1])
K = int(input_data[2])

def MaxTeam(N, M, K) :
    max_team = 0
    for i in range(K+1) :
        G = N - i
        B = M - (K - i)
        if (G >= 2*B) :
            if (B > max_team) :
                max_team = B
        else :
            if (G // 2 > max_team) :
                max_team = G // 2
    return max_team

print(MaxTeam(N, M, K))