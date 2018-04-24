from collections import defaultdict as dd

dp = dd(lambda: dd(lambda: 0))

N, M = [int(x) for x in input().split()]
cost = [int(x) for x in input().split()]
choice = dd(lambda: dd(lambda: 0))
cost = sorted(cost, reverse=True)
cost.insert(0, 0)
flag = dd(lambda: False)
# dp[i][j] 表示使用0-i范围内的钱币，总价值达到的最大值
for i in range(1, N):
    for v in range(M, cost[i] - 1, -1):
        if dp[i][v] <= dp[i - 1][v - cost[i]] + cost[i]:
            dp[i][v] = dp[i - 1][v - cost[i]] + cost[i]
            choice[i][v] = 1
print('123')
if dp[N - 1][M] != M:
    print("No Solution")
else:
    k = N
    num = 0
    v = M
    while k >= 0:
        if choice[k-1][v] == 1:
            flag[k-1] = True
            v -= cost[k]
            num += 1
        else:
            flag[k] = False
            k -= 1
    for i in range(N, 0, -1):
        if flag[i]:
            print(cost[i])
