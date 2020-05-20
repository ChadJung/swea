t = int(input())
par = ['(', ')', '{', '}']
stk = []
for tc in range(1, t+1):
    ans = True
    raw = input()
    text = [c for c in raw if c in par]
    for c in text:
        if par.index(c) % 2 == 0: # open
            stk.append(c)
        else: # close
            if len(stk) == 0 or par.index(stk[-1]) // 2 != par.index(c) // 2:
                ans = False
                break
            else:
                stk.pop()
    res = 1 if ans and not len(stk) else 0

    print(f'#{tc} {res}')