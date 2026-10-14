nums = [2,6,1,7,8,4,5,3,9]
for x in range(0, len(nums), 1):
    for y in range(x + 1, len(nums), 1):
        if nums[x] > nums[y]:
            nums[x], nums[y] = nums[y], nums[x]
print(nums)
