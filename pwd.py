def solve():
    cnt = 0
    while True:
        lst.append(lst.pop(0))
        lst[-1] -= cnt + 1
        if lst[-1] < 1:
            lst[-1] = 0
            return
        cnt = (cnt + 1) % 5


for tc in range(1, 11):
    input()
    lst = list(map(int, input().split()))
    solve()
    ans = ' '.join(str(i) for i in lst)
    print(f'#{tc} {ans}')