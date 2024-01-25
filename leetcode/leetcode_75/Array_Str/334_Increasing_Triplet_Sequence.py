#Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

#I think we can do this by keeping track of values and comparing. 
#for the last example we have init 2, then next is 1. any sequence where 2, y, z is valid, 1, y, z is also valid. We also know any sequence 2 , 1 , z is invalid so we can just remove 2 from the pool at make 1 the smallest number, and second smallest is now None
#We then hit 5, is not smaller than 1 so we make it the second smallest (1,5,z). 
#We hit 0 next which is smaller than both so we make it smallest (0,y,z). If say the number was 4 instead. We see that it is smaller than the second smallest but not smaller than the first so we make it now (1,4,z) any sequence 1,5,z would be valid with 1,4,z. 
#Once we have a scenario with x,y,z we can terminate and say true. 
#[2, None, None] -> [1,None,None] -> [1,5,None] -> [0,None,None] -> [0,4,None] -> [0,4,6] Terminate 
from math import inf

def solution(nums):

    first = nums[0]
    second = float('inf') #None #, (inf)
    third = float('inf') #None #(inf)
    idx = 1
    
    while idx <len(nums):
        if nums[idx] < first:
            first = nums[idx]
            second = float('inf')
            third = float('inf')
        elif nums[idx] < second:
            second = nums[idx]
            third = float('inf')
        elif nums[idx] < third:
            return True
        idx +=1
    
    print(first,second,third)
    #This breaks if there are less than 
    return False

nums = [2,1,5,0,4,6]
nums = [2]
nums = [20,100,10,12,5,13] #will break since we run out of entries, after 5
nums = [20,100,10,12,5,13,6] #will break since we go 5, 13 , 6 and return false when 10,12,13 is available 
nums = [10,12,5,13,13,13,13,13]
nums = [5,13,13,13]
nums = [1,2,5,4]
nums = [3,6,4,5]



# print(solution(nums))
        


def solutions(nums):

    first = nums[0]
    second = float('inf') #None #, (inf)
    third = float('inf') #None #(inf)
    idx = 1

    term_num = None
    
    while idx <len(nums):
        if term_num and nums[idx] >=term_num:
            print(first,second,nums[idx])
            return True
        elif nums[idx] < first:
            #There is another case here
            if second < float('inf'):
                term_num = second+1
            first = nums[idx]
            second = float('inf')
            third = float('inf')
        elif nums[idx] < second and nums[idx] > first:
            second = nums[idx]
            third = float('inf')
        elif nums[idx] < third and nums[idx] > second:
            print(first,second,third)
            return True
        idx +=1

    print(term_num)
    print(first,second,third)
    return False

nums = [20,100,10,12,5,13] #will break since we run out of entries, after 5
#nums = [20,100,10,12,5,13,6] #will break since we go 5, 13 , 6 and return false when 10,12,13 is available 
# nums = [10,12,5,13,13,13,13,13]
# nums = [5,13,13,13]

print(solutions(nums))

def increasingTriplet(nums):
        smallest = float('inf')
        middle = float('inf')
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= middle:
                middle = n
            else:
                return True

        return False

print(increasingTriplet(nums))