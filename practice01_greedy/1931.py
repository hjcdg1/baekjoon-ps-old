N = int(input())
SF = []
for _ in range(N) :
    SF_input = input().split()
    SF.append((int(SF_input[0]), int(SF_input[1])))
SF.sort(key = lambda t : t[0])
SF.sort(key = lambda t : t[1])

j = 0
cnt = 0
prev_f = 0

while (True) :
    while (j < N and not (SF[j][0] >= prev_f)) :
        j = j + 1

    if (not j == N) :
        cnt = cnt + 1
        prev_f = SF[j][1]
        j = j + 1
    else :
        break

print(cnt)
