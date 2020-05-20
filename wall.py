t = int(input())
for tc in range(1, t+1):
    n, a, b = map(int, input().split())
    result = float('inf')
    for c in range(1, int(n ** 0.5) + 1):
        for r in range(n//c + 1):
            eq = a * abs(r-c) + b *(n - r * c)
            result = eq if eq < result else result

    print(f'#{tc} {result}')