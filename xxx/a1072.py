from collections import defaultdict as dd
G = dd(lambda: dd(lambda: 0))
vis = dd(lambda: False)

def dijkstra(s):
  d = dd(lambda: 10**9)
  d[s] = 0
  vis = dd(lambda: False)
  for i in range(len(G)):
    u = min([v for v in G if not vis[v]], key=lambda v: d[v], default = -1)
    vis[u]=True
    if u==-1:return
    for v in G[u]:
      if not vis[v]:
        if d[u]+G[u][v]<d[v]:
          d[v]=d[u]+G[u][v]
  return d

tempPath, path = [], []
def dfs(d):
    global gas_list
    for u in d:
        if d[u]>Ds and u not in gas_list:
            return False
    return True

N,M,K,Ds = [int(x) for x in input().split()]
for i in range(K):
  p1, p2, dist = input().split()
  dist = int(dist)
  G[p1][p2]=G[p2][p1]=dist

gas_list = [s for s in G if s[0]=='G']
gas_valid = []
mean_dist = Ds / N
min_dist = 0
min_ind = M+1
for gas in gas_list:
    d = dijkstra(gas)
    d = {u:d[u] for u in d if u not in gas_list}
    if dfs(d):
        tmp = min(d.values()), sum(d.values())/len(d)
        if tmp[1]<mean_dist or int(gas[-1])<min_ind:
            min_ind=int(gas[-1])
            min_dist = tmp[0]
            mean_dist = tmp[1]
if min_ind == M+1:
    print("No Solution")
    exit(0)
print('G{}'.format(min_ind))
print('{:.1f}'.format(min_dist), '{:.1f}'.format(mean_dist))




"""
4 3 11 5
1 2 2
1 4 2
1 G1 4
1 G2 3
2 3 2
2 G2 1
3 4 2
3 G3 2
4 G1 3
G2 G1 1
G3 G2 2
"""