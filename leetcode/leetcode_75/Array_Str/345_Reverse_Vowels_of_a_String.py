# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



#Go through the array, have 1 pointer at the start and 1 at the end
#starting at the start pointer 
#check if the value in vowel set if it isnt increment the pointer
#if it is in the vowel set, we then go to the end pointer and check if it is the set. 
#If it isnt we decrement the counter 
#if it is then we swap the values and restart. 

def reverseVowels(s):

    start_idx = 0
    end_idx = len(s)-1

    vowel_set = ['A','E','I','O','U','a','e','i','o','u']

    char_list = list(s)
    #list in python are immutable change s to char_list
    while start_idx < end_idx:
        
        if char_list[start_idx] in vowel_set:
            val = char_list[start_idx]

            if char_list[end_idx] in vowel_set:
                char_list[start_idx] = char_list[end_idx]
                char_list[end_idx] = val
                end_idx-=1
                start_idx +=1
            else:
                end_idx-=1
        else:    
            start_idx +=1
    new_s = ("".join(char_list))
    return new_s

if __name__ == '__main__':
    string = "hello"
    string = 'leetcode'
    print(reverseVowels(string))