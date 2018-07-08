"""
思路比较奇特。构建 2sum hashmap，{2sum:[i,j]}:，
然后在 2sum 中查找另一半 {target-2sum:[k,m]}，配对，去重。
"""
from collections import defaultdict as dd
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        cache = dd(lambda :[])
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                cache[nums[i]+nums[j]].append([i, j])

        res, vis = [], {key: False for key in cache}
        for key in cache:
            if vis[key] or target - key not in cache:
                continue
            vis[key] = vis[target-key] = True

            for first_2 in cache[key]:
                for second_2 in cache[target-key]:
                    if set(first_2) & set(second_2):
                        continue
                    ans = sorted([nums[i] for i in first_2 + second_2])
                    if ans not in res:
                        res.append(ans)
        return res


def foo():
    nums = [1, 0, -1, 0, -2, 2]
    # nums = [0,0,0,0]
    target = 0
    solution = Solution()
    res = solution.fourSum(nums, target)
    print(res)


if __name__ == '__main__':
    foo()
