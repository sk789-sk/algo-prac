
#this question is basically asking as I keep adding the values in the array find the max since we start at 0

def solution(arr):
    start = 0
    current_max = 0 
    for val in arr:
        start += val
        current_max = max(start,current_max)

    return current_max


arr = [-5,1,5,0,-7]
arr2 = [-4,-3,-2,-1,4,3,2]
print(solution(arr))
print(solution(arr2))

