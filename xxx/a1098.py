# 堆排序

N = int(input())
nums = [int(x) for x in input().split()]
target = [int(x) for x in input().split()]

tmp = nums[:]
for i in range(2, N):
    if sorted(nums[:i]) + nums[i:] == target:
        print("Insertion Sort")
        print(' '.join(map(str, sorted(nums[:i + 1]) + nums[i + 1:])))
        exit(0)

print("Heap Sort")
nums.insert(0, 0)
target.insert(0, 0)


def downAdjust(low, high):
    i = low
    j = 2 * i
    while j < high:
        if j + 1 < high and nums[j + 1] > nums[j]:
            j += 1
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = j, 2 * j
        else:
            break


def heapSort():
    for i in range(N // 2, 0, -1):
        downAdjust(i, N)
    for i in range(N, 1, -1):
        nums[1], nums[i] = nums[i], nums[1]

        downAdjust(1, i)
        # print(nums)
        if nums == target:
            nums[1], nums[i - 1] = nums[i - 1], nums[1]
            downAdjust(1, i - 1)
            print(' '.join(map(str, nums[1:])))
            exit(0)


heapSort()

"""
https://www.patest.cn/contests/pat-a-practise/1098

Sample Input 1:

10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

Sample Output 1:

Insertion Sort
1 2 3 5 7 8 9 4 6 0

Sample Input 2:

10
3 1 2 8 7 5 9 4 6 0
6 4 5 1 0 3 2 7 8 9

Sample Output 2:

Heap Sort
5 4 3 1 0 2 6 7 8 9


"""
