for tc in range(1, 11):
    n = int(input())
    bur = list(map(int, input().split()))

    for _ in range(n):
        max_num, min_num = max(bur), min(bur)
        max_idx, min_idx = bur.index(max_num), bur.index(min_num)
        bur[max_idx] -= 1
        bur[min_idx] += 1

    print(f'#{tc} {max(bur) - min(bur)}')