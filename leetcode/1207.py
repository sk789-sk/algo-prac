# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

def solution(arr):
    keydict = dict()
    for val in arr:
        if val in keydict.keys():
            keydict[val]+=1
        else:
            keydict[val] = 1
    totalvals = list(keydict.values())
    print(totalvals)
    return len(totalvals) == len(set(totalvals))

t1 = [1,2,2,1,1,3]
t2 = [1,2]

print(solution(t1))
print(solution(t2))