from collections import defaultdict as dd
from copy import deepcopy


class BCG():
    def __init__(self):
        self.family = {}

    def findFather(self, x):
        a = x
        while x != self.family[x]:
            x = self.family[x]
        while a != x:
            a, self.family[a] = self.family[a], x
        return x

    def Union(self, a, b):
        fA = self.findFather(a)
        fB = self.findFather(b)
        if fA != fB:
            self.family[fA] = fB



G = dd(lambda: dd(lambda: 0))
vis = dd(lambda: False)
Family = BCG()

def load_data():
    N = int(input())
    for i in range(N-1):
        c1, c2 = [int(x) for x in input().split()]
        G[c1][c2] = 1
        G[c2][c1] = 1
        if c1 not in Family.family: Family.family[c1] = c1
        if c2 not in Family.family: Family.family[c2] = c2
        Family.Union(c1, c2)
    root = 0
    for i in Family.family:
        if Family.findFather(i)==i:
            root += 1
    if root > 1:
        print("Error: {} components".format(root))
        exit(0)
    return N


def dfs(u, state, currDepth):
    vis[u] = True
    if currDepth > state['maxDepth']:
        state['maxDepth'] = currDepth
        state['Node'] = [u]
    elif currDepth == state['maxDepth']:
        state['Node'].append(u)
    for v in G[u]:
        if not vis[v]:
            dfs(v, state, currDepth + 1)


N = load_data()
# 如果连通图数量 = 1，对于图中的每一个节点深搜，判断节点深度。
u = 1
state = {'maxDepth': 0, "Node" :[]}
dfs(u, state, 0)
set_a = state['Node'][:]

state = {'maxDepth': 0, "Node" :[]}
u = set_a[0]
for v in vis:
    vis[v] = False
dfs(u, state, 0)
set_b = state['Node'][:]

set_a.extend(set_b)
res = sorted(list(set(set_a)))
for it in res:
    print(it)
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
