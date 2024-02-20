# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
    total = sum(nums)
    idx = 0

    val_left = 0 
    val_right = total-nums[idx] 
    if val_left == val_right:
        return idx
    else:
        idx = 1
        while idx < len(nums):
            val_left = total-val_right
            val_right = val_right - nums[idx]
            
            if val_left == val_right:
                return idx
            idx+=1
    return -1
    # while idx < len(nums):
    #     if val_left == val_right:
    #         return idx
    #     idx+=1
    #     val_left = total-val_right
    #     val_right = val_right - nums[idx]
    #     print(val_left, val_right, idx)

t_arr = [1,7,3,6,5,6]
# t_arr = [1,2,3]
# t_arr = [2,-1,1]
print(pivotIndex(t_arr))


