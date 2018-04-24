from collections import defaultdict as dd
G = dd(lambda :dd(lambda :0))
cost = dd(lambda :dd(lambda :0))
vis = dd(lambda :False)
weight = dd(lambda : 0)
def dijkstra(s):
    d = dd(lambda :10**9) # 存放起始点到当前点的最小距离
    d[s] = 0 # 初始化
    c = dd(lambda :10**9)
    c[s] = 0
    pre = {} # 记录当前节点的前驱节点
    for i in range(len(G)):
        # 寻找使d[u]最小的还未被访问的u。
        u = min([v for v in G if not vis[v]], key=lambda v: d[v])
        vis[u] = True
        # 以u为中继，更新每个目标点的最小距离
        for v in G[u]:
            if not vis[v] and d[u]+G[u][v] < d[v]:
                d[v] = d[u] + G[u][v]
                c[v] = c[u] + cost[u][v]
                pre[v] = u
    return d, pre

def dijkstra_with_cost(s):
    d = dd(lambda :10**9)
    d[s] = 0
    c = dd(lambda: 10 ** 9)
    c[s] = 0
    pre = {}
    for i in range(len(G)):
        u = min([v for v in G if not vis[v]], key=lambda v: d[v])
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    c[v] = c[u] + cost[u][v]
                    pre[v] = u

                elif d[u] + G[u][v] == d[v] and c[u] + cost[u][v] < c[v]:
                    c[v] = c[u] + cost[u][v]
                    pre[v] = u
    return d, pre, c


def dijkstra_with_point_weight(s):
    d = dd(lambda: 10 ** 9)
    d[s] = 0
    w = dd(lambda : 0)
    w[s] = weight[s]
    for i in range(len(G)):
        u = min([v for v in G if not vis[v]], key=lambda v: d[v])
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                if d[u]+G[u][v]<d[v]:
                    d[v] = d[u] + G[u][v]
                    w[v] = w[u] + weight[v]
                elif d[u]+G[u][v] == d[v] and w[u] + weight[v] > w[v]:
                    w[v] = w[u] + weight[v]
    return d, w


def dijkstra_n_paths(s):
    d = dd(lambda: 10 ** 9)
    d[s] = 0
    w = dd(lambda : 0)
    w[s] = weight[s]

    for i in range(len(G)):
        u = min([v for v in G if not vis[v]], key=lambda v: d[v])
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                if d[u]+G[u][v]<d[v]:
                    d[v] = d[u] + G[u][v]
                    w[v] = w[u] + weight[v]
                elif d[u]+G[u][v] == d[v] and w[u] + weight[v] > w[v]:
                    w[v] = w[u] + weight[v]
    return d, w


def dfs(s, v, pre):
    if v==s:
        print(s)
        return
    dfs(s, pre[v], pre)
    print(v)

def dfs2(s, v, pre):
    stack = []
    while v!=s:
        stack.append(v)
        v = pre[v]
    stack.append(s)
    print(list(reversed(stack)))

def load_data():
    N,M,S = [int(x) for x in input().split()]
    for i in range(M):
        u, v, w = [int(x) for x in input().split()]
        G[u][v] = w
    d, pre = dijkstra(S)
    print(d)
    print(dfs2(S, 5, pre))

load_data()
"""
6 8 0
0 1 1
0 3 4
0 4 4
1 3 2
2 5 1
3 2 2
3 4 3
4 5 3
"""