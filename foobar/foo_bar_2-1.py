# Power Hungry============

# Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. 

#You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not take down all of the panels at once if you can help it, since they do help power the space station and all!You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is.

#Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".

#Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the solution as a string representation of the number.

# Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

# Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

# Input/output operations are not allowed.

# Your solution must be under 32000 characters in length including new lines and other non-printing characters.

##############################

#Ok so this is basically asking me to find the maximum number I can create with all the numbers in the array. by multiplication. 
#i would want ot multiply the largest numbers, remove all 0s and if i have an uneven number of negative numbers remove the largest negative number (-1). 

#so basicall as we go over the array we find the largest negative number. If we have an uneven number of negative numbers we can divide by that number. If we have an even number we can just ignore it  

#If it wants a subarray than we probably need to remove the smallest positive number

from math import inf

def solution(xs):
    #We need a subset
    #1. If we have an array of only 1 number return that number
    #2. If we have an array with a negative number and rest are 0 return 0. 
    #3. If we have only 0's return 0 
    #3. If we have all positive numbers multiply out
    #4. We have a 0 and not case 2 remove the 0s and multiply out
    #5. we have an odd number of negative numbers (-1,-1,2,4424,42424), remove largest non neg
    #6. We have an even numer of negative numbers, multiple out

    if len(xs) == 1:
        return str(xs[0])
    

    base = 1
    largest_neg = -999999
    number_of_neg = 0
    zero_c = 0

    for val in xs:
        if val ==0:
            zero_c +=1
            continue

        if val < 0:
            number_of_neg+=1
            largest_neg = max(largest_neg,val)

        base*=val

    if zero_c==len(xs):
        return str(0) 
    
    #Case if 1 neg and the rest are 0.

    if largest_neg !=-999999 and zero_c+1 == len(xs):
        return str(0) 

    if number_of_neg %2 !=0:
        base = base//largest_neg

    return str(base)

arr = [-1,-3,-9,5,6,7,0]
# arr = [2,0,2,2,0]
# arr = [-2, -3, 4, -5]
arr = [-1,0,0]


print(solution(arr))


# Input:solution.solution([2, 0, 2, 2, 0])Output:    8

# Input:solution.solution([-2, -3, 4, -5])Output: