from collections import defaultdict as dd
from copy import deepcopy

G = dd(lambda :dd(lambda :0))
vis = dd(lambda :0)

class BCG():
    def __init__(self):
        self.family = {}

    def findFather(self, x):
        a = x
        while x != self.family[x]:
            x = self.family[x]
        while a!=self.family[a]:
            a, self.family[a] = self.family[a], x
        return a

    def Union(self, a, b):
        fA = self.findFather(a)
        fB = self.findFather(b)
        if fA != fB:
            self.family[fA] = fB


def load_data():
    N = int(input())
    bcg = BCG()
    for i in range(N-1):
        n1, n2 = [int(x) for x in input().split()]
        G[n1][n2] = 1
        G[n2][n1] = 1
        if n1 not in bcg.family: bcg.family[n1] = n1
        if n2 not in bcg.family: bcg.family[n2] = n2
        bcg.Union(n1, n2)
    root = 0
    for i in bcg.family:
        if bcg.findFather(i) == i:
            root += 1
    if root > 1:
        print("Error: {} components".format(root))


def dfs(u, maxDepth, currDepth, maxNode):
    vis[u] = True

    if currDepth > maxDepth:
        maxDepth = currDepth
        maxNode = [u]
    elif currDepth == maxDepth:
        maxNode.append(u)

    for v in G[u]:
        if not vis[v]:
            dfs(v, maxDepth, currDepth+1, maxNode)


load_data()
u = 1
maxNode = [[]]
dfs(u, 0, 0, maxNode)
print(maxNode)
"""
5
1 2
1 3
1 4
2 5

5
1 3
1 4
2 5
3 4
"""
