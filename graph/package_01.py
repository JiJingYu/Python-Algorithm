from collections import defaultdict as dd

n, V = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

dp = dd(lambda :dd(lambda :0))
for i in range(1, n):
    for v in range(w[i], V+1):
        dp[i][v]=max(dp[i-1][v], dp[i-1][v-w[i]]+c[i])
print(dp[n-1][V])
"""
5 8
3 5 1 2 2
4 5 2 1 3
"""