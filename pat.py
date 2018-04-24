from collections import defaultdict, Counter


class BCG():
    def __init__(self):
        self.father = {}

    def findFather(self, x):
        tmp = x
        while self.father[x] != x:
            x = self.father[x]
        while tmp != self.father[tmp]:
            tmp, self.father[tmp] = self.father[tmp], x
        return x

    def Union(self, a, b):
        fA = self.findFather(a)
        fB = self.findFather(b)
        if fA != fB:
            self.father[fA] = fB


def foo():
    N = int(input())
    fat = BCG()
    people = [0 for i in range(N)]
    for i in range(N):
        tmp = [int(x) for x in input().split()[1:]]
        people[i] = tmp[0]
        for t in tmp:
            if t not in fat.father:
                fat.father[t] = t
        for j in range(1, len(tmp)):
            fat.Union(tmp[j], tmp[j - 1])

    count = Counter([fat.findFather(p) for p in people])
    ret = sorted(count.values(), reverse=True)
    print(len(ret))
    print(' '.join(map(str, ret)))


foo()
