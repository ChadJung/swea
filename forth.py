def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 / num2

t = int(input())
op = ['+', '-', '*', '/']
for tc in range(1, t+1):
    error = False
    stk = []
    text = input().split()
    for t in text:
        if t == '.':
            break
        if t not in op:
            stk.append(int(t))
        else:
            if len(stk) < 2:
                error = True
                break
            num2 = stk.pop()
            num1 = stk.pop()
            result = calc(num1, num2, t)
            stk.append(result)
    if len(stk) == 1:
        ans = stk[0]
    else:
        error = True
    prt = 'error' if error else ans
    print(f'#{tc} {prt}')
