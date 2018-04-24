from collections import defaultdict as dd
from collections import deque

G = dd(lambda :dd(lambda :0))

def bfs(u, L):
    q = deque([(u, 0)])
    inq = dd(lambda: False)
    inq[u] = True
    # Do something
    count = 0
    while q:
        u, level = q.popleft()
        for v in G[u]:
            if level == L or inq[v]:
                continue
            q.append((v, level+1))
            inq[v] = True
            count += 1
    return count


def load_data():
    N, L = [int(x) for x in input().split()]
    for i in range(1, N+1):
        follow = [int(x) for x in input().split()[1:]]
        # G[i][j] 表示j是i的follower
        for p in follow:
            G[p][i] = 1
    concern = [int(x) for x in input().split()[1:]]
    return concern, L


concern, L = load_data()
for p in concern:
    count = bfs(p, L)
    print(count)
"""
7 3
3 2 3 4
0
2 5 6
2 3 1
2 3 4
1 4
1 5
2 2 6
"""