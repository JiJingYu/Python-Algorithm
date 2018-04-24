# 插入排序
import bisect
def insert_(nums, i):
    # i start from 1
    s, s_no = nums[:i], nums[i+1:]
    bisect.insort_left(s, nums[i])
    return s+s_no
#并查集
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

# 最短路径
def dijkstra(s):
    d = dd(lambda :10**9)
    d[s] = 0
    pre = dd(lambda :[])

    for i in range(len(G)):
        u = min([v for v in G if not vis[v]], key=lambda v: d[v], default=-1)
        if u==-1: return
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    pre[v].clear()
                    pre[v].append(u)
                elif d[u] + G[u][v] == d[v]:
                    pre[v].append(u)
    return pre
tempPath = []
optvalue = -1
nums = 0
path = None
def calc(tempPath):
    global weight
    return sum(weight[p] for p in tempPath)
def dfs(s, v):
    global optvalue, nums, tempPath, path, pre
    if v == s:
        tempPath.append(v)
        nums += 1
        value = calc(tempPath)
        if value > optvalue:
            optvalue = value
            path = tempPath[:]
        tempPath.pop()
        return
    tempPath.append(v)
    for u in pre[v]:
        dfs(s, u)
    tempPath.pop()

# 堆排序

# 