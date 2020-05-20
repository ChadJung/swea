class Tree:
    def __init__(self, n, l):
        self.lst = [0] * (n+1)
        self.l = l

    def getNodeVal(self, num):
        if self.lst[num] == 0:
            if n >= num * 2 + 1:
                self.lst[num] = self.getNodeVal(num * 2) + self.getNodeVal(num * 2 + 1)
            else:
                self.lst[num] = self.getNodeVal(num * 2)
        return self.lst[num] 

    def getResult(self):
        self.getNodeVal(1)
        return self.lst[l]

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = Tree(n, l)
    for _ in range(m):
        idx, val = list(map(int, input().split()))
        tree.lst[idx] = val
    
    print(f'#{tc} {tree.getResult()}')
