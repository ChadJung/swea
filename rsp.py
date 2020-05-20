def win(x,y):
    X, Y = lst[x-1], lst[y-1]
    if X == Y or (X == 1 and Y == 3) or (X == 2 and Y == 1) or (X == 3 and Y == 2):
        return x
    return y

def match(start, end):
    if start == end:
        return start

    left = match(start, (start + end)//2)
    right = match((start + end)//2 + 1, end)
    return win(left, right)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    start = 1
    end = n
    print(f'#{tc} {match(start, end)}')
    