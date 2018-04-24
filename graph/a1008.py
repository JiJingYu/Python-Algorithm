nums = [int(x) for x in input().split()[1:]]

prev = 0
total_time = 0
for i in range(len(nums)):
    diff = nums[i]-prev
    if diff >0:
        total_time += diff * 6
    else:
        total_time -= diff * 4
    prev = nums[i]
total_time += len(nums)*5
print(total_time)
