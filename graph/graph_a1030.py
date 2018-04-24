from collections import defaultdict as dd
G = dd(lambda :dd(lambda : 0))
cost = dd(lambda :dd(lambda : 0))
vis = dd(lambda :False)

def dijkstra(s):
    d = dd(lambda :10**9)
    d[s]=0
    pre = dd(lambda :[])
    for i in range(len(G)):
        u = min([v for v in G if not vis[v]], key=lambda v:d[v], default=-1)
        if u==-1:return
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    pre[v].clear()
                    pre[v].append(u)
                elif d[u] + G[u][v] == d[v]:
                    pre[v].append(u)
    return pre

tempPath, path = [], []
optvalue = 10** 9

def dfs(s, v):
    global pre, tempPath, path, optvalue
    if v == s:
        tempPath.append(v)
        value = sum([cost[tempPath[i]][tempPath[i-1]] for i in range(len(tempPath)-1, 0, -1)])
        if value < optvalue:
            path = tempPath[:]
            optvalue = value
        tempPath.pop()
        return
    tempPath.append(v)
    for u in pre[v]:
        dfs(s, u)
    tempPath.pop()

N,M,S,D = [int(x) for x in input().split()]
for i in range(M):
    c1, c2, dst, cos = [int(x) for x in input().split()]
    G[c1][c2]=G[c2][c1] = dst
    cost[c1][c2] = cost[c2][c1] = cos

pre = dijkstra(S)
dfs(S, D)
total_dist = sum(G[path[i]][path[i-1]] for i in range(len(path)-1, 0, -1))
total_cost = optvalue
print(' '.join(map(str, reversed(path))), total_dist, total_cost)
# path, total distance, total cost