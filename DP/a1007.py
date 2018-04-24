# 8.56-9.14,20min
N=int(input())
nums = [int(x) for x in input().split()]
if max(nums)<0:
    print(0, nums[0], nums[-1])
    exit(0)
if len(nums)==1:
    print(nums[0],nums[0],nums[0])
    exit(0)

# f[i]=max(f[i-1]+nums[i], nums[i])
f=[0 for _ in nums]
f[0] = nums[0]
s=[0 for __ in nums]
s[0] = nums[0]
for i in range(1, len(nums)):
    if f[i-1]<0:
        f[i]=nums[i]
        s[i]=nums[i]
    else:
        f[i]=f[i-1]+nums[i]
        s[i]=s[i-1]
max_f = max(f)
for i in range(len(f)):
    if f[i]==max_f:
        print(max_f, s[i], nums[i])
        exit(0)
# max_f = max(f)
# for i in range(len(f)):
#     if f[i]==max_f:
#         tmp = max_f
#         for j in range(i, -1, -1):
#             tmp -= nums[j]
#             if tmp==0:
#                 print(max_f, nums[j], nums[i])
#                 exit(0)

"""
6
-2 11 -4 13 -5 -2 
"""