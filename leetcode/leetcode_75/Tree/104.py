# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#We need to traverse this tree and everytime we go down we need to keep track of it.


def solution(node, depth = 0):
    if not node:
        return depth
    left = solution(node.left, depth= depth +1)
    right = solution(node.right, depth= depth +1)
    return max(left,right)

def solution2(node, depth=0):
    if not node:
        return depth
    left = solution(node.left, depth + 1)
    right = solution(node.right, depth + 1)
    return max(left, right)

root = TreeNode(3)
root.left = TreeNode(9)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(173)
# root.left.right.right = TreeNode(-1)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(solution(root))