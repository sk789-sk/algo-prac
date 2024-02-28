# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

#Question is asking me how many K sums are present 

#If we sort the array first we can then start form the ends we can then pull out sums as more the idx. 

def solution(arr,k):
    sorted_arr = sorted(arr)
    l_idx = 0
    r_idx = len(arr) - 1
    pairs = 0
    
    while sorted_arr[r_idx] >= k and r_idx >0:
        r_idx -=1 

    while l_idx < r_idx:
        if sorted_arr[l_idx] + sorted_arr[r_idx] == k:
            l_idx +=1 
            r_idx -=1
            pairs +=1 
        elif sorted_arr[l_idx] + sorted_arr[r_idx] > k:
            r_idx -=1
        else:
            l_idx +=1
    return pairs

test1 = [1,2,3,4]
test2 = [3,1,3,4,3]
solution(test1,5)
solution(test2,6)

