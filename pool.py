def solve(n, s):
    global result
    if n >= 12:
        if s < result:
            result = s
    else:
        solve(n + 1, s + day * monthly[n])
        solve(n + 1, s + mth)
        solve(n + 3, s + tri)



t = int(input())
for tc in range(1, t+1):
    day, mth, tri, year = map(int, input().split())
    monthly = list(map(int, input().split()))
    result = year

    solve(0, 0)
    print(f'#{tc} {result}')