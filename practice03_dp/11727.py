n = int(input())

def tile_case(n) :
    D = [0 for _ in range(n+2)]
    D[0] = 1
    D[1] = 3
    for i in range(2, n) :
        D[i] = 2 * D[i-2] + D[i-1]
    return D[n-1]

print(tile_case(n) % 10007)