N = int(input())

def PinaryNumber(n) :
    D = [0 for _ in range(n+2)]
    D[0] = 1
    D[1] = 1
    D[2] = 2

    # 2 * D[i-1] : 맨 뒤에 0 혹은 1을 붙이는 경우
    # - D[i-3] : 하지만 맨 뒤가 011인 경우는 제외해줘야 함
    for i in range(3, n) :
        D[i] = 2 * D[i-1] - D[i-3]

    return D[n-1]

print(PinaryNumber(N))