def dfs(row):
    global min_val, total

    if total > min_val:
        return

    if row == n:
        min_val = total
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = 1
            total += lst[row][col]
            dfs(row + 1)
            visited[col] = 0
            total -= lst[row][col]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_val = 91
    total = 0
    dfs(0)
    print(f'#{tc} {min_val}')