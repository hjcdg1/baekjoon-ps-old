T = int(input())
input_list = [0 for _ in range(T)]
for t in range(T) :
    input_list[t] = int(input())

def SumCase(n) :
    M = [0 for _ in range(n + 1)]
    M[0] = 1
    M[1] = 1
    for i in range(2, n + 1) :
        sum = M[i - 1]
        if (i >= 2) :
            sum += M[i - 2]
        if (i >= 3) :
            sum += M[i - 3]
        M[i] = sum
    return M[n]

for t in range(T) :
    print(SumCase(input_list[t]))