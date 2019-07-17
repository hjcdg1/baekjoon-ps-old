NK = input().split()
N = int(NK[0])
K = int(NK[1])
V = []
for _ in range(N) :
    V.append(int(input()))

left_money = K
i = N-1
cnt = 0
while (left_money != 0) :
    n = left_money // V[i]
    if (n != 0) :
        cnt = cnt + n
        left_money = left_money - n * V[i]
    else :
        i = i - 1

print(cnt)
