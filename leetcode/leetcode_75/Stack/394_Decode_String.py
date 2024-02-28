# <!-- Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105. -->


#approach is we keep it all within the stack. and at the end the stack will represent the string
#append characters from the string to the stack until we encounter a ]. 
#Once we encounter that we pop characters until we hit a [. This sequence represents the string that may be multiplied. 
#we then pop the characters after the [ which will be digits until we see that the preceding value is not a digit.
#We then multiply the number with the encoded string and then append that to the stack. 
#We then continue down the original string. 
#Once the string is fully traversed we have only characters in the stack representing the string after it has been decoded.
#Turn the stack into a string and then return it.  

def solution(s):
    stack = []
    for val in s:
        if val != ']':
            stack.append(val)
            print(stack)
        else: #we have encountered ]
            #we pop until the first [ and find the multiples of it. expand the string and then add that to the stack.
            encoded_str = ''
            char = stack.pop()

            while char != '[':
                #we pop    
                if char.isalpha():
                    encoded_str = char + encoded_str
                    print(encoded_str)
                char = stack.pop()         

            if char == '[':
                print('la')
                num = stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack[-1] + num
                    stack.pop()

                full_str = int(num) * encoded_str
                print(full_str)
                for char in full_str:
                    stack.append(char)

    print(stack)
    out_str = "".join(stack)
    print(out_str)
    return(out_str)


t1 = '3[a]2[bc]'
t1 = "3[a2[c]]"
t1 = "2[abc]3[cd]ef"
t2 = "100[lee]"
t1 = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
t1 = 'abcd'

solution(t1)