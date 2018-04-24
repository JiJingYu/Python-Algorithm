import array
import random
import time
color_d = array.array('i', [random.randint(0, 210) for i in range(210)])
# color_d =array.array('i', [int(x) for x in input().split()])
nums = array.array('i', [random.randint(0, 420) for i in range(20000)])
nums = array.array('i', [num for num in nums if num in color_d])
# nums = array.array('i', [int(x) for x in input().split()])
start = time.time()
dp = [[0 for i in nums] for j in color_d]
# 2. 最长公共子序列
for i in range(1, len(color_d)):
    for j in range(1, len(nums)):
        dp[i][j]=max(dp[i-1][j], dp[i][j-1])+int(nums[j]==color_d[i])
print(dp[-1][-1])
end = time.time()
print(end-start)
"""
6
5 2 3 1 5 6
12 2 2 4 1 5 5 6 3 1 1 5 6
"""