

    # Your code here
    #could try this recursively cut it in half and check if its ok, we then cut in half third/4th until no more options 
    #so like abcabcabcbc goes to abcabc vs abcabc. split = 2
    #now check if abcabc can be split which can be abc split = 2
    #now see if abc can be split into half, no, thirds yes but a!=b!=c so we know it cant be split any further.
    #Multuply the splits together to get 4.
    
    #abadabadabad
    #abadab, adabad != so we try 3. 
    #abad ==  abad == abad so split =3
    
    
    
    #if value is prime it cant be split evenly. We could find the factors for the character length and see say 12 then we could have 2,3,4,6,12. This is better than trying say 1-12
    
    #once we have the factors of the number we start from the lowest and go up intil we get a case that all the strings produced at equal to each other
    #once we have a number that meets this criteria we take note of the number and we repeat this with the substring.
    #We repeat this process until a substring cannot be split into any even values. 
    #At that point we multiply all the numbers we got for spliiting and that gives us the total number of splits. 
    
    #abadabadabad ex: len=12
    #we get the factors(prime?) for 12, 1,2,3,4,6,12 I think prime factors is better 6 would get caught bby the 2/3 first we need to ignore 1 as well
    
    #so we split the stirng into 2 resulting in abadab adabad. These are not equal so now we try again with 3. 
    #so we get abad abad abad. We see the 3 are equal so we know we can split into size 3. [1,3]
    
    #now we have abad so factors are 1,2,4 prime only is 2. 
    #split abad into 2 so we get ab ad. Compare the 2 and we see that they are equal. 
    
    #we cannot split anymore so we multiply 1*3 to get 3 splits is the maximum. 
    
    #abababababababababababab" len=24
    #string='abababababababababababab' factors= 2,3,4,6,8,12 split = [1]
    #string = 'abababababab' factors =2,3,4,6, split = [1,2]
    #string = 'ababab' factors = 2,3, splot = [1,2,2]
    #string = 'ab' factors = 1,2 split = [1,2,2,3]
        
    
    
    
    #"abcdeabdceabcde" len = 15


def solution(s):

    number_of_splits = 1
    split = 2

    while split <= (len(s)):
        test_set = set()
        if len(s) % split ==0:
            splitpoint = int(len(s)/split)        
            parts = [s[i:i+splitpoint] for i in range(0, len(s), splitpoint)]

            for val in parts:
                test_set.add(val)
            
            if len(test_set)==1:
                number_of_splits = number_of_splits * split
                split = 2
                s = s[0:splitpoint]
            else:
                split +=1                
        else:
            split = split +1
    # print(number_of_splits)
    return number_of_splits
            

def solutions(s):
    #just check forever, we want the most so if we jsut start from 0 and go to the end itll go.
    for i in range(len(s)+1):
        check = s[:i]
        number = s.count(check)
        if number * check == s:
            return number
    return 1

       
s = 'abababababababababababb'
       
print(solutions(s) == solution(s))    


print(solution(s))

print(solutions(s))
    


