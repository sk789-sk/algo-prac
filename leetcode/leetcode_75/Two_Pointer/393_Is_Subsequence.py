# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#"" is a subsequence of everything including and empty string. 


def solution(s,t):
    if len(s) == 0:
        return True

    t_idx = 0
    s_idx = 0

    while t_idx <len(t):
        if s[s_idx] == t[t_idx]:
            s_idx += 1
            t_idx += 1
            if s_idx == len(s):
                return True
        else:
            t_idx+=1

    return False

s = 'abc'
t = 'ahgbdc'

print(solution(s,t))