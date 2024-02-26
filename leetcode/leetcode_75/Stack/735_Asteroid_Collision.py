# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

from collections import deque

def solution(asteroids):
    
    stack = [] 

    for val in asteroids:
        while stack and stack[-1] >0 and val < 0: #+,- scenario where crash occurs
            total = stack[-1] + val
            if total > 0:
                val = 0 #None < 0 is not valid so lets make val = 0 
            elif total ==0:
                stack.pop()
                val = 0
            else:
                stack.pop()
                # stack.append(val)
                #this needs to check again as well basically rerun it.        
        if val != 0:
            stack.append(val) #all other cases(+,+) (-,-) (-,+)
    
    print(stack)
    return stack


array  = [5,10,5]
array2 = [8,-8]
array3 = [10,2,-5]
array4 = [5,10,-11]

solution(array)
solution(array2)
solution(array3)
solution(array4)