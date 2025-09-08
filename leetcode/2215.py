# #Find the Difference of Two Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

def solution(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return[list(set1-set2), list(set2-set1)]


t1 = [1,2,3]
t2 = [2,4,6]

t3 = [1,2,3,3]
t4 = [1,1,2,2]
print(solution(t1,t2))
print(solution(t3,t4))