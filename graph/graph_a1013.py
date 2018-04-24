from collections import defaultdict as dd
G = dd(lambda: dd(lambda: 0))
vis = dd(lambda: False)
def dfs(u, city):
    vis[u] = True
    for v in G[u]:
        if not vis[v]:
            dfs(v, city)
N, M, K = [int(x) for x in input().split()]
for i in range(M):
    c1, c2 = [int(x) for x in input().split()]
    G[c1][c2] = G[c2][c1] = 1
for city in input().split():
    city = int(city)
    for u in G:
        vis[u] = False
    vis[city] = True
    n_graph = 0
    for u in G:
        if not vis[u]:
            n_graph += 1
            dfs(u, city)
    print(n_graph - 1)

"""
3 2 3
1 2
1 3
3 2 1


3 2 2
1 2
1 3
2 3
"""
