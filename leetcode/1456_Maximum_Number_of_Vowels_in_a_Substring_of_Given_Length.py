# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

def solution(s,k):
    vowel_set = set(['a','e','i','o','u'])
    init_str = s[:k]
    count = 0

    for char in init_str:
        if char in vowel_set:
            count +=1

    maxcount = count
    if maxcount==k:
        return k

    for i in range(k,len(s)):
        next_char = s[i]
        kicked_char = s[i-k]

        if next_char in vowel_set:
            count +=1
        if kicked_char in vowel_set:
            count -=1   
        if count > maxcount:
            maxcount = count
            if maxcount == k: #might not be worth
                return k
    
    return maxcount

test_arr = "leetcode"

x = solution(test_arr,3)
print(x)