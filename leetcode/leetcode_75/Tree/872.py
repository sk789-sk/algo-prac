# 872. Leaf-Similar Trees

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

#We can use DFS traversal to get the leafs of the tree. A node is a leaf it both its left and right values are equal to None. 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root1,root2):
    def getLeafValueSeq(root):
        leaf_arr = []

        def traverse(root):
            if not root:
                return 
            if not root.left and not root.right:
                leaf_arr.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return leaf_arr
    
    r1arr = getLeafValueSeq(root1)
    r2arr = getLeafValueSeq(root2)
    return r1arr==r2arr

def solution2(root1,root2):
    #Lets try this with a stack
    stack = deque()
    stack.append(root1)
    l1 = deque()
    while stack:
        node = stack.popleft()
        if not node.left and not node.right:
            l1.append(node.val)
        if node.right:         
            stack.appendleft(node.right) 
        if node.left:
            stack.appendleft(node.left)
    stack.append(root2)
    
    #better approach at this point would be to compare the values in the l1 list and node and terminate early if they do not match
    while stack:
        node = stack.popleft()
        if not node.left and not node.right: #not a child
            if len(l1) == 0:
                return False
            val = l1.popleft()
            if val != node.val:
                return False
        if node.right:         
            stack.appendleft(node.right) 
        if node.left:
            stack.appendleft(node.left)    
    return len(l1) == 0  ##If L1 still has value after going through all of the second tree they are not equal. 

test = TreeNode(3)
test.left = TreeNode(5)
test.right = TreeNode(1)
test.left.left = TreeNode(6)
test.left.right = TreeNode(2)
test.left.right.left = TreeNode(7)
test.left.right.right = TreeNode(4)
test.right.left = TreeNode(9)
test.right.right = TreeNode(8)



test2 = TreeNode(3)
test2.left = TreeNode(5)
test2.right = TreeNode(1)
test2.left.left = TreeNode(6)
test2.left.right = TreeNode(7)
test2.right.left = TreeNode(4)
test2.right.right = TreeNode(2)
test2.right.right.left = TreeNode(9)
test2.right.right.right = TreeNode(8)
print(solution2(test, test2))