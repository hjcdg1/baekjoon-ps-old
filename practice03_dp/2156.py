n = int(input())
amount = [0 for _ in range(n+2)]
for i in range(n) :
    amount[i] = int(input())

def max_amount(n, amount) :
    # D[i] : i번째 포도주까지 고려했을 때, 최대로 마실 수 있는 포도주 양

    D = [ 0 for _ in range(n+2) ]
    D[0] = amount[0]
    D[1] = amount[0] + amount[1]
    D[2] = max(amount[0] + amount[2], amount[1] + amount[2], amount[0] + amount[1])
    for i in range(3, n) :
        D[i] = max(D[i-1], D[i-2] + amount[i], D[i-3] + amount[i-1] + amount[i])
    return D[n-1]

print(max_amount(n, amount))