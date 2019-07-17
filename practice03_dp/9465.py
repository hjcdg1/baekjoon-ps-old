T = int(input())
n = []
fst = []
snd = []
for t in range(T) :
    n.append(int(input()))
    input_data_1 = input().split()
    input_data_2 = input().split()
    fst.append([ int(input_data_1[i]) for i in range(n[t]) ])
    snd.append([ int(input_data_2[i]) for i in range(n[t]) ])

def max_point(n, fst, snd) :
    D = [ [0, 0] for _ in range(n) ]
    D[0][0] = fst[0]
    D[0][1] = snd[0]
    D[1][0] = snd[0] + fst[1]
    D[1][1] = fst[0] + snd[1]

    for i in range(2, n) :
        D[i][0] = max(D[i-1][1] + fst[i],
                      D[i-2][0] + fst[i],
                      D[i-2][1] + fst[i])
        D[i][1] = max(D[i-1][0] + snd[i],
                      D[i-2][0] + snd[i],
                      D[i-2][1] + snd[i])

    return max(D[n-1][0], D[n-1][1])

for t in range(T) :
    print(max_point(n[t], fst[t], snd[t]))