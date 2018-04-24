from collections import defaultdict
def foo1():
    # 双指针，尾指针+头指针
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums[i:]):
            print(num, num2)


# 知识点1：defaultdict 默认值
# 知识点2：max函数默认值
# 知识点3：双指针：尾指针+头指针
class Solution:
    def maxPoints(self, points):
        max_len = 0
        for i, p1 in enumerate(points):
            dic = defaultdict(lambda: 1)
            same = 1
            for j, p2 in enumerate(points[:i]):
                dx, dy = p2.x - p1.x, p2.y - p1.y
                if dx == 0 and dy == 0:
                    same += 1
                else:
                    slope = 'inf' if dx == 0 else dy / dx
                    dic[slope] += 1
            max_len = max(max_len, max(dic.values(), default=1) + same)
        return max_len


# 知识点4：统计序列中每个元素出现的次数：Counter

if __name__ == '__main__':
    foo1()
