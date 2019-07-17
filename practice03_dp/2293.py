input_data = input().split()
n = int(input_data[0])
k = int(input_data[1])
v = [ int(input()) for _ in range(n) ]
v.sort()

def coin_case(n, k, v) :
    D = [0 for _ in range(k+1)]

    D[0] = 1    # 아무것도 고르지 않는 경우는 1가지이다.

    # i번째 동전까지만 고려했을 때의 D값을 구한다.
    for i in range(n) :
        for j in range(1, k+1) :
            if (v[i] <= j) :
                D[j] += D[j-v[i]]

    return D[k]

print(coin_case(n, k, v))