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


def dijkstra(s, weight):
    d = dd(lambda :10**9)
    d[s] = 0
    nums = dd(lambda :0)
    nums[s] = 1
    w = dd(lambda :0)
    w[s] = weight[s]

    for i in range(len(G)):
        u = min([v for v in G if not vis[v]], key=lambda v: d[v])
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    w[v] = w[u] + weight[v]
                    nums[v] = nums[u]
                elif d[u] + G[u][v] == d[v]:
                    nums[v] += nums[u]
                    if w[u] + weight[v]>w[v]:
                        w[v] = w[u] + weight[v]
    return nums, w


C1, C2, weight = load_data()
nums, w = dijkstra(C1, weight)
print(nums[C2], w[C2])


