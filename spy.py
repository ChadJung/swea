def verify(pwd):
    odd = pwd[0::2]
    even = pwd[1:7:2]
    v = pwd[-1]
    return sum(pwd) if (v + (sum(odd) * 3 + sum(even))) % 10 == 0 else 0

def codeToNum(code):
    dic = {
            '0001101' : 0,
            '0011001' : 1,
            '0010011' : 2,
            '0111101' : 3,
            '0100011' : 4,
            '0110001' : 5,
            '0101111' : 6,
            '0111011' : 7,
            '0110111' : 8,
            '0001011' : 9
    }
    pwd = [0] * 8
    for i in range(8):
        pwd[i] = dic[code[i * 7: (i + 1) * 7]]

    return pwd


t = int(input())
for tc in range(1, t+1):
    rows, cols = map(int, input().split())
    
    for _ in range(rows):
        row = input()
        if '1' in row:
            code = row

    for i in range(cols - 1, -1, -1):
        if code[i] == '1':
            code = code[i-55:i+1]
            break
    
    print(f'#{tc} {verify(codeToNum(code))}')
