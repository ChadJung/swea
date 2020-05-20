class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self, num):
        if num > 1:
            if self.lst[num] < self.lst[num//2]:
                self.lst[num], self.lst[num//2] = self.lst[num//2], self.lst[num]
                self.sort(num//2)

    def append(self, value):
        num = len(self.lst)
        self.lst.append(value)
        self.sort(num)
    
    def getSum(self, node):
        if node > 1:
            return self.lst[node] + self.getSum(node//2)
        else:
            return self.lst[node]

    def solve(self):
        last = len(self.lst) - 1
        if last > 1:
            return self.getSum(last//2)
        else:
            return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    tree = Tree()
    for i in map(int, input().split()):
        tree.append(i)
    print(tree.lst)
    print(f'#{tc} {tree.solve()}')