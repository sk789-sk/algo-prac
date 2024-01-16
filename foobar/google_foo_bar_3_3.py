#You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.

#But there's a few catches. First, the bombs self-replicate via one of two distinct processes: Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;Every Facula bomb spontaneously creates a Mach bomb.For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

#Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

#You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.


#Ok so at each generation we can create F bombs equal to the nunmber of M bombs and M bombs equal to the number of F bombs. It saying produce made me thing its like we are creating this many but that doesnt make sense.

#We can see that for each generation we work towards it by adding the smaller number to the larger nnumber. we can work backwards knowing this:

#For the example where we need 4 F bombs and 7 M bombs. 
#The only way to get to 7 M bombs and 4 F bombs is to have 4 F bombs and 3 M bombs the generation beforehand
#From that logic the only way to get to 4F bombs would be to have 3 M bombs and 1 F bombs beforehand.
#That leads to 2 M bombs and 1 F bomb and then 1 M bomb and 1F bomb which is the starting position. 

#If we have some number n bombs and the other is 1 we need n-1 generations to get to n bombs. 
#If we ever have 2 equal number of bombs and the count is not equal to 1 it owuld be impossible starting at 1-1 since they would always be differing by at least 1. 
#This actually extends further is we had 9 M: 3 F that would be impossible to get to as well. General rule ends up bieng if n > m and n mod m == 0 it is unsolavble. 

#something else is that if we have 21 m bombs and 4 f bombs. We would go 21-17-13-9-5-1. 
#What this really is is 21 divide by 4. The whole nunmber is the number of generations and the remainder is the new value to reach. if n > m generation count = floor(n/m) , and leftover is n % m that we continue with. this would assume that n/m is a positive number as well. 

from math import floor

def solution(n,m):

    generations = 0

    n = int(n)
    m = int(m)

    while n >=1 or m >=1:
        print(f' n = {n} m = {m}')
        if n == 1 or m == 1:
            generations += max(n,m) -1
            return generations

        #check if possible 

        if (max(n,m) % min(n,m)) == 0:
            return -1

        #Case where we now work out way down:
        n,m = max(n,m) ,min(n,m)
        # m = min(n,m)
        generations += floor(n/m)
        n = n % m

        print(f' generations={generations} n = {n} m = {m}')



        # larger = max(n,m)
        # smaller = min(n,m)
        # generations += floor(larger/smaller)
        # larger = larger % smaller
        
test = ('4','7')

print(solution(*test))



#2.7 

def solutions(n,m):

    generations = 0

    n = int(n)
    m = int(m)
    

    while n >=1 or m >=1:
        
        if n == 1 or m == 1:
            generations += max(n,m) -1
            return str(generations)

        #check if possible 

        if (max(n,m) % min(n,m)) == 0:
            return 'impossible'

        #Case where we now work out way down:
        n,m = max(n,m) ,min(n,m)
        # m = min(n,m)
        generations += n//m  #2.7 returns a float maybe thats causing the issue?
        n = n % m
        
        # larger = max(n,m)
        # smaller = min(n,m)
        # generations += floor(larger/smaller)
        # larger = larger % smaller


print(solutions('4','7'))