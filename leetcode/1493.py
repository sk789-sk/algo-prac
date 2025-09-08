# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

#Ok this works the same way as the sliding windows problem with k = 1. We start but going through the array until we hit our second 0. At which point we have the max len of that run we then move the lag to the first 0 we saw for that and continue.

def solution(nums):
    lead = 0 
    lag = 0
    max_len = 0
    curren_len = 0
    dels = 0
    #maxflips=1

    while lead < len(nums):
        if nums[lead] == 0:
            dels+=1

        while dels > 1:
            if nums[lag] == 0:
                dels -=1
            lag+=1
        curren_len = lead - lag + 1
        if curren_len > max_len:
            max_len = curren_len
        lead+=1

    print(max_len-1)
    return max_len-1

test = [1,1,0,1]
solution(test)
t2 = [0,1,1,1,0,1,1,0,1]
solution(t2)
t3 = [1,1,1]
solution(t3)