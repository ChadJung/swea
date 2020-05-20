for tc in range(10):
    buildings = list(map(int, input().split()))
    light_sum = 0
    for i in range(2, len(buildings) - 2):
        cut = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if buildings[i] - cut > 0:
            light_sum += buildings[i] - cut
    print(f'#{tc} {light_sum}')