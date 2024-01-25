#Given an array return the products of all the elements other than itself.

#Must be O(n) time and cannot use the division operations. 


#If i could use division then the example would be easy just multiple all the numbers together and then divide by the index. 
#Specific cases would be if there is a single 0 in the array then when we get to that digit the value is the array multuples
#if there are 0 zeroes then all the values are equal to 0. 

#If we cannot use division the value is equal to the multiplication of all values. We would check all values but this would have alot of repeat values and would have iterate over the array multiple times. This would push n^2 

#The value is also equal to the product of all values to the left and the right of the digit.
#If we keep track of these values for each number we could do this in 3 passes through the array. First go left to right to get all the values on the left side of a digit. Second pass go from finish to start to get all values to the right side. Finally 1 last pass checking the values against each other. This would also make it so we dont care about the edge cases witht the 0 since its accoutned for.  
#Feel like theres a way to do this in fewer but w.e

#Ex: arr = [1,2,3,4,5]

#Lets multiply all numbers with the previous value
#arr1 = [1,2,6,24,120] Going left to right
#arr2 = [120,120,60,20,5] Going Right to Left

#Then to check the value of an idx we take the arr1[idx-1] * arr2[idx+1] =


def solution(arr):
    left_arr = len(arr)*[0]
    left_arr[0] = arr[0]
    right_arr = len(arr)*[0]
    right_arr[-1] = arr[-1]

    counter = 1
    while counter <len(arr):
        left_arr[counter] = left_arr[counter-1] * arr[counter]
        counter +=1

    # for idx, val in enumerate(arr):        
    #     left_arr[idx] = left_arr[max(idx-1,0)] * val #Issue with wraparound, useing max to make sure we never to to negative, 

    #Could find the length and iterate from -1 to -len

    counter = -2

    while counter >= -1* len(arr):
        right_arr[counter] = right_arr[min(counter+1,-1)] * arr[counter]
        counter -=1

    # for idx,val in enumerate(reversed(arr)):
    #     print( idx,val)

    #Have the 2 arrays with the values


    out_arr = [0] * len(arr)

    for idx,_ in enumerate(arr):
        left = left_arr[idx-1] if idx-1 >=0 else 1
        right = right_arr[idx+1] if idx+1<len(arr) else 1 
        out_arr[idx] = left*right

    print(left_arr)
    print(right_arr)    
    return out_arr

nums = [-1,1,0,-3,3]

print(solution(nums))




