class Tree:
    def __init__(self, N):
        self.lst = [0] * (N + 1)
        self.N = N
        self.cnt = 1
        self.numbering(1)

    def numbering(self, num):
        if num <= self.N:
            self.numbering(num * 2)
            self.lst[num] = self.cnt
            self.cnt += 1
            self.numbering(num * 2 + 1)

    def my_result(self):
        return ' '.join(map(str, (self.lst[1], self.lst[self.N // 2])))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    tree = Tree(n)
    print(f'#{tc} {tree.my_result()}')