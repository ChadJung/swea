def solve(now, cost):
    global result
    if cost > result:
        return

    if now == 0 and sum(visited) < n - 1:
        return

    visited[now] = 1
    if now == 0 and sum(visited) == n:
        result = min(cost, result)
        visited[now] = 0
        return

    for nextNode in range(n):
        if not visited[nextNode]:
            solve(nextNode, cost + costMap[now][nextNode])
    visited[now] = 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    costMap = [list(map(int, input().split())) for _ in range(n)]
    result = 1101
    for start in range(1, n):
        visited = [0] * n
        solve(start, costMap[0][start])
    print(f'#{tc} {result}')