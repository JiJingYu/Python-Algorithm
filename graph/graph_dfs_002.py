from collections import defaultdict as dd

G = dd(lambda: dd(lambda: 0))
W = dd(lambda: 0)
vis = dd(lambda: False)
vis_e = dd(lambda: dd(lambda: False))


def load_data():
    N, k = [int(x) for x in input().split()]
    for i in range(N):
        p1, p2, w = [x for x in input().split()]
        w = int(w)
        G[p1][p2] += w
        G[p2][p1] += w
        W[p1] += w
        W[p2] += w
    return k


def dfs(u, graph_weight, paths):
    vis[u] = True
    paths[-1].append(u)
    for v in G[u]:
        if not vis_e[v][u]:
            vis_e[u][v] = True
            vis_e[v][u] = True
            graph_weight[-1] += G[u][v]

    for v in G[u]:
        if not vis[v]:
            dfs(v, graph_weight, paths)


def dfs_trave(graph_weight, paths):
    for u in G:
        if not vis[u]:
            graph_weight.append(0)
            paths.append([])
            dfs(u, graph_weight, paths)


k = load_data()
graph_weight = []
paths = []
dfs_trave(graph_weight, paths)
res = []
for i in range(len(paths)):
    if graph_weight[i] > k and len(paths[i]) > 2:
        leader = max(paths[i], key=lambda d: W[d])
        res.append((leader, len(paths[i])))
res = sorted(res, key=lambda d: d[0])
print(len(res))
for it in res:
    print(it[0], it[1])