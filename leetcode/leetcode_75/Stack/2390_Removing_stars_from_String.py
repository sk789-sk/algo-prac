# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

#Given a string we keep adding values to the stack. when we encounter a star value we popright on the stack instead of appending

from collections import deque

def removestar(s):
    output = ''
    for val in s:
        if val !='*':
            output+=val
        else:
            output = output[:-1]
    return output

def removestar_deque(s):
    output = deque('')
    for val in s:
        if val !='*':
            output.append(val)
        else:
            output.pop()
    out_str = "".join(output)
    return str(out_str)


test_s = "leet**cod*e"

removestar_deque(test_s)