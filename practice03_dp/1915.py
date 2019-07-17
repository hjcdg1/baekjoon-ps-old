input_data = input().split()
n = int(input_data[0])
m = int(input_data[1])
A = [ [0] * (m+1) for _ in range(n+1) ]
for i in range(1, n+1) :
    input_data = input()
    for j in range(1, m+1) :
        A[i][j] = int(input_data[j-1])

def max_rect_area(n, m, A) :
    D = [ [0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if (A[i][j] == 0) :
                D[i][j] = 0
            elif (A[i-1][j] == 0 or A[i][j-1] == 0 or A[i-1][j-1] == 0) :
                D[i][j] = 1
            else :
                D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1

    max_ = float('-inf')
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            temp = D[i][j] * D[i][j]
            if (temp > max_) :
                max_ = temp

    return max_

print(max_rect_area(n, m, A))