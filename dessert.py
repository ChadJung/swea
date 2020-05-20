def prom(x, y):
    return (0 <= x < n) and (0 <= y < n)


def solve(x, y, direction, count):
    global result
    if (x, y) == (start_x, start_y) and direction == 3:
        result = max(result, count)
    elif not prom(x, y):
        return
    elif course[y][x] in ate:
        return
    else:
        ate.append(course[y][x])
        if direction in [0, 1]:
            solve(x + dirX[direction], y + dirY[direction], direction, count + 1)
            solve(x + dirX[direction + 1], y + dirY[direction + 1], direction + 1, count + 1)
        elif direction == 2:
            if x + y != start_x + start_y:
                solve(x + dirX[direction], y + dirY[direction], direction, count + 1)
            else:
                solve(x + dirX[direction + 1], y + dirY[direction + 1], direction + 1, count + 1)
        else:
            solve(x + dirX[direction], y + dirY[direction], direction, count + 1)
        ate.pop()




t = int(input())
for tc in range(1, t+1):
    n = int(input())
    course = [list(map(int, input().split())) for _ in range(n)]

    ate = []

    result = -1
    dirX = [1, -1, -1, 1]
    dirY = [1, 1, -1, -1]
    
    for x in range(1, n-1):
        for y in range(0, n-1):
            start_x, start_y = x, y
            ate.append(course[start_y][start_x])
            solve(start_x + 1, start_y + 1, 0, 1)
            ate.pop()

    print(f'#{tc} {result}')