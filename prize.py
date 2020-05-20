def dfs(now, swap):
    global result, c
    if swap == c:
        result = max(result, int(''.join(num)))
        return

    for i in range(now, len(num)):
        for j in range(i + 1, len(num)):
            if num[i] <= num[j]:
                num[i], num[j] = num[j], num[i]
                c -= 1
                dfs(i, swap + 1)
                num[i], num[j] = num[j], num[i] 
    

t = int(input())
for tc in range(1, t+1):
    num, c = input().split()
    c = int(c)
    num = list(num)
    result = 0
    dfs(0, 0)
    print(f'#{tc} {result}')
