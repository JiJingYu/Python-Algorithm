from collections import defaultdict as dd

G = dd(lambda :dd(lambda :0))
vis = dd(lambda :False)

def load_data():
    N,M,C1,C2 = [int(x) for x in input().split()]
    weight = [int(x) for x in input().split()]
    for i in range(M):
        c1, c2, L = [int(x) for x in input().split()]
        G[c1][c2] = G[c2][c1] = L
    return C1, C2, weight


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


C1, C2, weight = load_data()
pre = dijkstra(C1)
dfs(C1, C2)
print(nums, optvalue)


"""
5 6 0 2
1 2 1 5 3
0 1 1
0 2 2
0 3 1
1 2 1
2 4 1
3 4 1
"""