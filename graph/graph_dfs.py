"""
图，可以用邻接矩阵表示。
G(V,E)表示图
数据结构方面，用嵌套字典表示
G[u,v] 表示边权
W[u]表示点权
vis[u]表示节点的访问记录
vis_e[u][v] 表示边的访问记录
"""
from collections import defaultdict as dd

G = dd(lambda :dd(lambda :0))
vis = dd(lambda :False)
W = dd(lambda :0)
vis_e = dd(lambda :dd(lambda :False))


def load_data():
    N, k = [int(x) for x in input().split()]
    for i in range(N):
        p1, p2, num = input().split()
        G[p1][p2] += int(num)
        G[p2][p1] += int(num)
        W[p1] += int(num)
        W[p2] += int(num)
    # for u in G:
    #     vis[u] = False
    #     for v in G[u]:
    #         vis_e[u][v] = False
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


def foo():
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





def test001():
    foo()


if __name__ == '__main__':
    test001()

"""
8 59
AAA BBB 10
BBB AAA 20
AAA CCC 40
DDD EEE 5
EEE DDD 70
FFF GGG 30
GGG HHH 20
HHH FFF 10
"""