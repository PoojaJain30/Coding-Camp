# move_zero

def move_zero(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums

print(move_zero([0,1,0,3,12]))