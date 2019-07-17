T = int(input())
input_list = []
for _ in range(T) :
    input_list.append(int(input()))

def tuple2string(t) :
    left = str(t[0])
    right = str(t[1])
    return left + " " + right

def fibonacci_cnt(n) :
    if (n == 0) :
        return (1, 0)
    elif (n == 1) :
        return (0, 1)
    elif (n >= 2) :
        F = [-1 for _ in range(n + 1)]
        cnt = [-1 for _ in range(n + 1)]
        F[0] = 0
        F[1] = 1
        cnt[0] = (1, 0)
        cnt[1] = (0, 1)

        for i in range(2, n + 1) :
            F[i] = F[i - 1] + F[i - 2]
            cnt[i] = (cnt[i -1][0] + cnt[i - 2][0], cnt[i - 1][1] + cnt[i - 2][1])
        return cnt[n]

for t in range(T) :
    print(tuple2string(fibonacci_cnt(input_list[t])))