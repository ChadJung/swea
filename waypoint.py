def dfs(start):
    global result
    visited[start] = 1
    for nxt in range(1, v+1):
        if edgeMap[start][nxt] and not visited[nxt]:
            if nxt == end_node:
                result = 1
                return
            dfs(nxt)

t = int(input())
for tc in range(1, t+1):
    
    v, e = map(int, input().split())
    visited = [0 for _ in range(v+1)]
    edgeMap = [[0] * (v+1) for _ in range(v+1)]

    for _ in range(e):
        start, end = map(int, input().split())
        edgeMap[start][end] = 1
    start_node, end_node = map(int, input().split())
    result = 0
    dfs(start_node)
    print(f'#{tc} {result}')

