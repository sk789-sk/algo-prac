# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

def solution(chars):
    #Ok i think we have to replace the chars array as we do it, but it also looks like we trim the array of all the excess stuff after putting in the string?
    #Does it want us to take the string and then break it down into its individual elements and have each of those as the array?
    #How is that constant space tho since the string grows with the size of the input?     
    s = ""
    replacement_idx = 0
    reading_idx = 1
    counter = 1
    current_char = chars[0]

    while reading_idx < len(chars):
        if chars[reading_idx] == current_char:
            counter +=1 
            reading_idx +=1
        else:
            if counter == 1:
                s+=current_char
                chars[replacement_idx] = current_char
                replacement_idx+=1
            else:
                s += current_char+str(counter)
                for idx,val in enumerate(current_char+str(counter)):
                    chars[replacement_idx+idx] = val

                replacement_idx+=len(current_char+str(counter))
            #for char in (current_char+str(counter)):
            
            current_char = chars[reading_idx]
            reading_idx += 1
            counter = 1

    #The last value needs to be added 
    if counter == 1: 
        s+=current_char
        chars[replacement_idx] = current_char
    else:
        s+=current_char+str(counter)
        for idx,val in enumerate(current_char+str(counter)):
            chars[replacement_idx+idx] = val


    return s , chars , len(s) , chars[0:len(s)]

test = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars_ = ['a']

print(solution(test))
print(solution(chars))
print(solution(chars_))