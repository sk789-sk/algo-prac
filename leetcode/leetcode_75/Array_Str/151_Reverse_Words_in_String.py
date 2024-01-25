# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

#start from the end chck if character is a whitespace, if it is continue. If not we take that idx keep it and then continue until we find a whitespace. Once we do we have a word and we add it to the string and 1 space. We then continue this process until we go through the entire string. 

def solution(s):

    idx = len(s)-1
    new_s = ""
    while idx >=0:
        if s[idx].isspace() is False:
            # print(s[idx],idx)
            wordend_idx = idx
            idx -=1 
            #in the case we have idx 0 we will break since we now are idx = -1 and we wrap around, we need to check for idx to be within bounds here as well 

            if idx <0:
                word = s[:wordend_idx+1]
                new_s += word
                return new_s

            while s[idx].isspace() is False:    
                idx -=1

                if idx <0:
                    word = s[:wordend_idx+1]
                    new_s += word
                    return new_s

            # print(s[idx+1:wordend_idx+1])
            new_s += f'{s[idx+1:wordend_idx+1]} '
        idx -=1
    # print(new_s[:-1])
    return new_s[:-1]
        

test_str = '   abc dba  '
input = "ab good   example"
input2 = "  hello world  "
i3 = 'a b ba'
print(solution(test_str))

print(solution(input))
print(solution(input2))
print(solution(i3))

