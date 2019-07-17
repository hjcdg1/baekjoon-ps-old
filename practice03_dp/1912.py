n = int(input())
input_data = input().split()
sequence = [0 for _ in range(n)]
for i in range(n) :
    sequence[i] = int(input_data[i])

def max_sequence(n, sequence) :
    D = [0 for _ in range(n)]

    D[0] = sequence[0]

    for i in range(1, n) :
        if (D[i-1] >= 0) :
            D[i] = D[i-1] + sequence[i]
        else :
            D[i] = sequence[i]

    max_ = D[0]
    for i in range(1, n) :
        if (D[i] >= max_) :
            max_ = D[i]

    return max_

print(max_sequence(n, sequence))