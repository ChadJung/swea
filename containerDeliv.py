t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    conts = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    ans = 0
    for truck in trucks:
        while conts:
            cont = conts.pop(0)
            if cont <= truck:
                ans += cont
                break
    print(f'#{tc} {ans}')
