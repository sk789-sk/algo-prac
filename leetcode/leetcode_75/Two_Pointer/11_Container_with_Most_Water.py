# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

#Want to maximize height and width. We can start with a max width but setting the idx to 0 and len. 
#To maximize height we are looking to minimize the distane between the 2 heights but also want them to be as large as possible. 


def maxArea(arr):
    l_idx = 0
    r_idx = len(arr)-1
    max_area = 0

    while l_idx < r_idx:


        area = (r_idx-l_idx) * min(arr[l_idx],arr[r_idx])
        print( f' {area = } {l_idx = } {r_idx =} {arr[l_idx] = } {arr[r_idx] = } ')
        max_area = max(max_area,area)
        
        # #move the idx
        
        
        #This is incorrect, just moving to the larger one doesnt do anything since we are limited by the size of the smaller one. If anything we want the opposite.
        # if arr[l_idx + 1] > arr[r_idx - 1]:
        #     l_idx +=1
        # else: #arr[l_idx] <=arr[r_idx]
        #     r_idx -=1

        if arr[l_idx] > arr[r_idx]:
            r_idx-=1
        else:
            l_idx +=1

    print(max_area)
    return max_area


arr = [2,3,4,5,18,17,6] #31

maxArea(arr)

arr2 = [1,3,2,5,25,24,5] #32 

print(f'testing {arr2}')

maxArea(arr2)


