n = int(input())

def TileCase(n) :
    # D[i] : i번째 컬럼까지 채우는 경우의 수
    D = [0 for _ in range(n+1)]
    D[0] = 1
    D[1] = 2

    # 1. D[i-1] : 2x1 타일 하나만 추가하는 경우
    # 2. 2 * D[i-2] : 2x1 타일 둘 혹은 1x2 타일 하나를 추가하는 경우
    # 3. - D[i-2] : 1번 경우와 2번 경우의 교집합 (맨 끝에 두 줄이 2x1 타일 둘인 경우)
    for i in range(2, n) :
        D[i] = D[i-1] + 2 * D[i-2] - D[i-2]

    return D[n-1]

print(TileCase(n) % 10007)
