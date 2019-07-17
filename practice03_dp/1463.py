X = int(input())

def MinOperation (X) :
    M = [0 for _ in range(X+1)]
    M[1] = 0
    for i in range(2, X + 1) :
        min = float('inf')
        if (i % 3 == 0) :
            if (M[i // 3] < min) :
                min = M[i // 3]
        if (i % 2 == 0) :
            if (M[i // 2] < min) :
                min = M[i // 2]
        if (M[i - 1] < min) :
            min = M[i - 1]
        M[i] = min + 1
    return M[X]

print(MinOperation(X))
