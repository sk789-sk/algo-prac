# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

#[0,0,0,0,0,0,0,0,0]

#we can slide along the array looking at idx-1, idx, idx+1. 

#If the idx value is 1 we move to idx+2. Reasoning here is that if this is 1 then the adjacent one cannot be.
#If the value of the idx is 0. If idx-1 is 0 and idx +1 is 0 then we make this idx value=1 and move to idx+2 since its now the same as case 1. We planted 1 flower so we can keep track of that.
#If the idx = 0, and idx-1 = 1 then we slide over 1 
#if the idx =1 and idx+1 = 1 we slide over 3. 
#how do we handle the edges, where the -1 and +1 are outside of the arr index. Those are the same as 0s

#Input: flowerbed = [1,0,0,0,1], n = 1

#Input: flowerbed = [1,0,0,0,1], n = 2

def canPlaceFlowers(flowerbed, n):
    
    if n==0:
        return True    

    #Could simplfy this probably but lazy
    if len(flowerbed) == 1 and flowerbed[0] == 1:
        return False
    
    if len(flowerbed) == 1 and flowerbed[0] == 0 and n==1:
        return True

    if flowerbed[0] == 1:
        idx = 2
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        n-=1
        if n == 0:
            return True
        idx = 2
    if flowerbed[0] == 0 and flowerbed[1] == 1:
        idx = 3





    while idx < len(flowerbed):
        prev = max(idx-1,0)
        next_ = min(idx + 1, len(flowerbed)-1) #of the final value

        #if sum of all 3 is 0 we go idx+2 n-1
        #if not we can just do idx+1 and its slower, but simpler

        if (flowerbed[idx]+flowerbed[prev]+flowerbed[next_]) == 0:
            n-=1
            flowerbed[idx] =1 #not needed since we jumping +2 and wont interact with it anymore
            idx +=2
            if n == 0:
                return True
        else:
            idx +=1            
    return False

if __name__ == '__main__':
    string1 = 'ABABABAB'
    string2 = 'ABABAB'

    arr = [1,0,0,0,1]
    num = 2

    print(canPlaceFlowers(arr,num))