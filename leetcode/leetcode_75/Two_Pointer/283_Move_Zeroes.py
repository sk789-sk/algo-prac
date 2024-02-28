# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


def moveZeroes(nums):
    zero_idx = []
    check_idx = 0

    while check_idx < len(nums):
        if nums[check_idx] == 0:
            zero_idx.append(check_idx)
        else:
            if len(zero_idx) == 0:
                check_idx+=1
                continue
            new_idx = zero_idx.pop(0)
            nums[new_idx] = nums[check_idx]
            nums[check_idx] = 0
            zero_idx.append(check_idx)
        check_idx+=1
    print(nums)

   
nums = [0,1,0,3,12]
test = [0]
test2 = [1,2,3,4,5]
moveZeroes(nums)
moveZeroes(test)
moveZeroes(test2)