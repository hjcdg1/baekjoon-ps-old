N = int(input())
W = []
for _ in range(N) :
    W.append(int(input()))
W.sort(reverse = True)

cnt = 1
prev_weight = 0

for i in range(N) :
    new_weight = (i+1) * W[i]

    if (new_weight >= prev_weight) :
        prev_weight = new_weight

print(prev_weight)
