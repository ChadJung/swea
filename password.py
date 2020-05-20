def solve():
    global k
    print(k)
    point = 0
    while k:
        point += m
        point %= len(lst)
        val = lst[(point-1) % len(lst)] + lst[point]
        if point == 0:
            lst.append(val)
            point = -1
        else:
            lst.insert(point, val)

        k -= 1

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    solve()
    print(f'#{tc}', end=' ')
    print(' '.join(str(n) for n in lst[-1:-11:-1]))