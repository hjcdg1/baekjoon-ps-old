N = int(input())
P = input().split()
P = [int(P[i]) for i in range(N)]
P.sort()
T = [0 for _ in range(N)]

T[0] = P[0]
P_sum = P[0]
sum = T[0]

for i in range(1, N) :
    T[i] = P_sum + P[i]
    P_sum = P_sum + P[i]
    sum = sum + T[i]

print(sum)
