t = int(input())
for tc in range(1, t+1):
    text = input()
    flag = True
    while flag:
        flag = False
        prev = text[0]
        for n, c in enumerate(text[1:]):
            if c == prev:
                text = text[:n] + text[n+2:]
                flag = True
                break
            else:
                prev = c
    ans = len(text)
    print(f'#{tc} {ans}')