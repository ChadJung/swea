def solve(row, col, S):
    global result
    if (row, col) == (n-1, n-1):
        result = min(result, S + vals[row][col])
        return

    if row + 1 < n:
        solve(row + 1, col, S + vals[row][col])
    if col + 1 < n:
        solve(row, col + 1, S + vals[row][col])


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    vals = [list(map(int, input().split())) for _ in range(n)]
    result = 260
    solve(0, 0, 0)
    print(f'#{tc} {result}')