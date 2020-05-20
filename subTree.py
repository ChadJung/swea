def solve(root):
    global count
    count += 1
    for next_node in edgeMap[root]:
        if next_node:
            solve(next_node)


t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    l = max(lst)

    edgeMap = [[0, 0] for _ in range(l + 1)]
    for i in range(len(lst)//2):
        idx = 1 if edgeMap[lst[i*2]][0] != 0 else 0
        edgeMap[lst[i*2]][idx] = lst[i*2+1]

    count = 0
    solve(n)
    print(f'#{tc} {count}')