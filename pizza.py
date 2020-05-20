t = int(input())
for tc in range(1, 1+t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    Q = []
    for i in range(n):
        Q.append([lst[i], i])

    i = 0
    while len(Q) != 1:
        Q[0][0] //= 2

        if Q[0][0] == 0:
            if n + i < m:
                Q.pop(0)
                Q.append([lst[n+i], n+i])
                i += 1
            else:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
    
    print(f'#{tc} {Q[0][1] + 1}')


