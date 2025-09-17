# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.


#We use DFS so we alwauys know the path to the node when we reach it. We can keep a stack of the values in the node visited and another value keeping track of the max value in the path. When we reach a leaf node and need to go back up we check if the value in that node is larger or equal to the max. If it is we then go through the stack to find the max and set it to that. If not we can continue. For each node we get to we check if its value is greater that or equal to the current max. If it is we increment our counter.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    counter = 0
    node_stack = deque()
    current_max = 0
    value_list = []
    node_stack.append(root)

    while node_stack:
        current_node = node_stack.pop()
        if current_node.val >= current_max:
            counter +=1
            current_max = current_node.val
        value_list.append(current_node.val)
        
        if not current_node.left and not current_node.right:
            #We are going back up so we need to do something here
            pass

        if current_node.right:
            node_stack.append(current_node.right)
        if current_node.left:
            node_stack.append(current_node.left)


    return counter


root = TreeNode(3,TreeNode(1,TreeNode(3)),TreeNode(4,TreeNode(1),TreeNode(6)))