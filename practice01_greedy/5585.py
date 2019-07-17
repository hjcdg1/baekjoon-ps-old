pay = int(input())
change = 1000 - pay
V = [500, 100, 50, 10, 5, 1]

left_money = change
i = 0
cnt = 0
while (left_money != 0) :
    n = left_money // V[i]
    if (n != 0) :
        cnt = cnt + n
        left_money = left_money - n * V[i]
    else :
        i = i + 1

print(cnt)
