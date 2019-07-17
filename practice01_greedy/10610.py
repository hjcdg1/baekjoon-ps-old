N_list = list(input().strip())
N_list.sort(reverse = True)
N_len = len(N_list)
N = int("".join(N_list))

# 10의 배수 체크
if (int(N_list[N_len-1]) == 0) :
    sum = 0
    for c in N_list[:N_len-1] :
        sum = sum + int(c)
    if (sum % 3 != 0) :
        print(-1)
    else :
        print(N)
        pass
else :
    print(-1)
