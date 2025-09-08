# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

#ok so we iterate over the array if we see a 1 we continue, if we see a 0 we flip continue but decrement out k couter. Once k goes to zero or we hit the end of the array we have the max run for that and we can save it.
#Now Where to start the next array. It would probably be from the first 0 we saw.

def solution(nums, k):
    
    lead = 0
    lag = 0
    max_len = 0
    curren_len = 0
    flips = 0

    while lead < len(nums):
        if nums[lead] == 0:
            flips +=1 

        while flips > k:
            #Move lag to the first 0     
            if nums[lag] == 0:
                flips -=1    
            lag +=1
        
        #Measure window Size and Update Max
        curren_len = lead - lag + 1
        if curren_len > max_len:
            max_len = curren_len
        lead +=1
    
    print(max_len)
    return max_len


if __name__ == "__main__":
    test = [1,1,1,0,0,0,1,1,1,1,0]
    test2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    solution(test2,3)