input_data = input().split()
A = input_data[0].strip()
B = input_data[1].strip()

def MinDiff(A, B) :
    A_len = len(A)
    B_len = len(B)
    min_diff = float('inf')

    for k in range(B_len - A_len + 1) :
        diff = 0
        for i in range(A_len) :
            if (A[i] != B[k+i]) :
                diff += 1
        if (diff < min_diff) :
            min_diff = diff
    return min_diff

print(MinDiff(A, B))