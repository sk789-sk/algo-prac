# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
#Okay i have 2 strings and we need to find the divisor for both of the strings. 

#Start with the smaller string check if it divides into the larger string.
#Then take the string and check it for possible divisors aka 1/2, 1/3, 1/4, 1/5... if something isnt 1/2 divisible then it cant be 1/4th divisible also so we just have to check each prime nnumber no?
#If we find a match we then check it against the other string, if we have 1 wthen we found the maximum. 

#We could also find the common divisors between the 2 strings. and the iterate over the maximums 



def solution(str1,str2):

    length = min(len(str1),len(str2))

    if length == len(str1):
        smaller,larger = str1, str2
    else:
        smaller, larger = str2, str1
    c = 1

    while c <=len(smaller):
        if len(smaller) % c == 0:
            potential_m = smaller[0:(len(smaller)//c)]
            if potential_m * c == smaller:
                if(len(larger)%len(potential_m)) == 0:
                    multiples = len(larger)//len(potential_m)
                    if(potential_m*multiples == larger):
                        return(potential_m)
        c+=1
    return ""


        

    

if __name__ == '__main__':
    string1 = 'ABABABAB'
    string2 = 'ABABAB'

    print(solution(string1,string2))
    print(solution('leet','code'))
    print(solution('ABCABC','ABC'))