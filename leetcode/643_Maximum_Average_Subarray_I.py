# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Ok we can take the first K values in the array into a FIFO que. SUM it up and that is the max value. record idx start(0) and idx end(k-1).
#Read along the next value in the array pop the out the first element in the FIFO que and add the newly read value to it. SUM it up. If its greater than the max then record the start and end idx and update the max. If not we just continue. Probably something better than summing up the values in fifo que. 


def calcArray(nums,k):

    current_sum = sum(nums[:k])
    maxval = current_sum


    for i in range(k,len(nums)):
        current_sum += nums[i] - nums[i-k]
        if current_sum > maxval:
            maxval = current_sum
        # maxval = max(current_sum,maxval)

    return maxval/k

if __name__ == "__main__":
    arr = [1,12,-5,-6,50,3]
    arr = [7,4,5,8,8,3,9,8,7,6]
    calcArray(arr,7) 