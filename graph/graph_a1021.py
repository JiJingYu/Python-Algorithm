from collections import defaultdict as dd
from copy import deepcopy

G = dd(lambda: dd(lambda: 0))
vis = dd(lambda: False)


def load_data():
    N = int(input())
    for i in range(N-1):
        c1, c2 = [int(x) for x in input().split()]
        G[c1][c2] = 1
        G[c2][c1] = 1
    return N


def dfs(u, depths, depth):
    vis[u] = True
    depths[-1][1] = max(depths[-1][1], depth)
    for v in G[u]:
        if not vis[v]:
            dfs(v, depths, depth + 1)


def dfs_trave():
    n_graph = 0
    depths = []
    for u in G:
        if not vis[u]:
            depths.append([u, 0])
            n_graph += 1
            dfs(u, depths, 1)
    return n_graph


N = load_data()
n_graph = dfs_trave()
# 判断连通图数量，如果数量>1, 输出错误并退出
if n_graph > 1:
    print("Error: {} components".format(n_graph))
    exit(0)
# 如果连通图数量 = 1，对于图中的每一个节点深搜，判断节点深度。
depths = []
for u in G:
    depths.append([u, 0])
    for v in vis: vis[v] = False
    dfs(u, depths, 1)
# print(depths)
max_d = max(i[1] for i in depths)
for i in depths:
    if i[1] == max_d:
        print(i[0])


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
