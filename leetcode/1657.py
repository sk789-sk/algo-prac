# # 1657. Determine if Two Strings Are Close

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


def solution(word1,word2):
    # @are they the same size? going to assume they are
    # Operation 1 means that if 2 strings have the same characters with same letter frequencies we can turn them into each other.
    # Operation 2 means that we can adjust the letter frequencies to another one that is the same, so we need the letter frequency values to be the same without any care for the letter. (a=1,b=2,c=3 and b=3,c=1,a=2) can work 
    # So iterate over the letters, keep track of the letters themselves and the values. this also checks that they are equal in length. I
    w1_dict = {}
    w2_dict = {}
    for char in word1:
        w1_dict[char] = w1_dict.get(char,0)+1
    
    for char in word2:
        w2_dict[char] = w2_dict.get(char,0)+1
    
    w1charset = set(list(w1_dict.keys()))
    w2charset = set(list(w2_dict.keys()))

    print(w1charset)
    print(w2charset)
    if (w1charset != w2charset):
        return False

    w1valuelist = list(w1_dict.values())
    w2valuelist = list(w2_dict.values())

    #Check if the 2 value lists have the same values, could order them and check if they are equal. We could work with sum I think since we are checking for equal character sets already. Nvm this won't work since if something has 3 and there are no 3s on the other we cannot match. 
    w1valuelist.sort()
    w2valuelist.sort()

    if (w1valuelist) == (w2valuelist):
        return True
    return False

w1 = 'abc'
w2 = 'bca'

w3 = 'a'
w4 = 'aa'

w5='cabbba'
w6='abbccc'

w7="cabbba"
w8="aabbss"

w9="abbzzca"
w10="babzzcz"

print(solution(w1,w2))
print(solution(w3,w4))
print(solution(w5,w6))
print(solution(w7,w8))
print(solution(w9,w10))