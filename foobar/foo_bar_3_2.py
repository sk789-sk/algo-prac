# In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in. Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

#brute force this by going for each x we check y if y divides x we then go to z and check for all z that divides y. 
#we could do this but i think we would be checking alot of things over and over again for no reason.


#first though is that if x divides y and y divides z then x also divides z. 
#If i took x and divided the entire array by it i would have some evenly divisible elements. [arr2]
#I look at the first evenly divisible element which would be my y and whatever value y is i would then divide the rest of the array by that. [arr3]
#At this point all array values that are evenly divisible would be lucky triples of x,y,z
#Would then move to the next evenly divisible value in arr2 and repeat the process
#would then have to do this for each value in the array. Theres probably a better way. 

#I guess the main thing here is that once we have an x and y that divide each other we have a condition for a lucky triple. 
#if we keep track of that condition we know whenever we hit a lucky triple. if we have [2,3,4,6...] we know that when we check 2 and 4 anything in the future that divies 4 is a lucky triple. we get to 2,6 anything that divides 6 is a lucky triple. We also see 3,6 and we know that anything that divides by 6 is actually creates 2 lucky triples, (2,6,x) and (3,6,x). We keep track of these conditions, whenever we get to a number we divide it by the number of lucky triples we get from 6.

#Ex: [2,3,4,5,6,8,12,24] 
#anything divisible by 4 check(2,3) creates 1 lucky triple. (2,4,x)
#anything divisible by 6 check(2,3,4,5) creates 2 lucky triples (2,6,x), (3,6,x)
#anything divisibly by 8 check(2...7) creates 2 lucky triples (2,8,x), (4,8,x)
#anything divisible by 12 check(2...11) creates 3 lucky triples (2,12,x), (3,12,x),(4,12,x),(6,12,x)
#anything divisble by 24 creates 6 (2,24,x),(3,24,x),(4,24,x),(6,24,x),(8,24,x),(12,24,x)

#any number creates max # of factors worth of triples, we need to see which ones are present in the array and check upto th emax of that number. 

def solution(arr):

    trackarr = [0] * len(arr) #if this is a dict we can make accessing this value 0(1) instead of O(n)
    
    count = 0
    track_dict = {}
    
    for i in range(len(arr)):
        track_dict[i] = 0
        for j in range(i):
            if arr[i] % arr[j] == 0:
                trackarr[i] +=1 
                count += trackarr[j]
    return count

testarr = [2,3,4,5,6,8,12,24]

testarr= [1,2,3,4,5,6]

print(solution(testarr))