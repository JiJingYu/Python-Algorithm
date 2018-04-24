# 1098. Insertion or Heap Sort
import bisect
def insert_(nums, i):
    # i start from 1
    s, s_no = nums[:i], nums[i+1:]
    bisect.insort_left(s, nums[i])
    return s+s_no
n=int(input())
nums = [int(x) for x in input().split()]
tag = [int(x) for x in input().split()]
tmp = nums[:]
for i in range(1, n-1):
    tmp = insert_(tmp, i)
    if tmp==tag:
        print("Insertion Sort")
        tmp = insert_(tmp, i+1)
        print(" ".join(map(str, tmp)))
        exit(0)
print("Heap Sort")