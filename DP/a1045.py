import array
N = int(input())
color_d = {c:i for i, c in enumerate(input().split())}
nums = array.array('i', [color_d[x] for x in input().split() if x in color_d])

# 2. 最长不下降子序列问题
dp=nums[:]
for i in range(len(nums)):
    dp[i]=max((dp[j]+1 for j in range(i) if nums[j]<=nums[i]), default=1)
print(max(dp))

"""
6
5 2 3 1 5 6
12 2 2 4 1 5 5 6 3 1 1 5 6
"""