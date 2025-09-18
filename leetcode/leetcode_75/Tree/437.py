# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

#what if each node keeps track of the nodes in its path. 
#We would be checking every path in the tree this way.
# We can keep track of the sums in the path so far. when we get to the node A,B,C,D when we get to d we have ABC,BC,C.
# Now when we get to a node we can check if the targetsum - value in the node is within the sums in the path (there can be duplicates). If it then we found a target path. 
# So if we have a path that goes 10 -> 5 -> 3 -? 3 when we get to the last 3 we should have the following values (18,8,3) given to it:
#We can then to k - 3 to get some value and if the value is in the dictionary passed to it great we have a path. If the value is in the dictionary 2 we have 2 values.
# We can then 

#We traverse down the tree in lets do DFS. For each node we keep a running sum of the values for the different ways to the node. That we when we get to the node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  


def solution(root,k):
    counter = 0 
    node_stack = deque([])
    init_dict = dict()
    node_stack.append((root, init_dict))

    #An issue with this is that when going through the stack we would be losing where we are if we do right then left. Need a different traversal path I think.

    while node_stack:
        current_node, sums_to_node = node_stack.pop()

        if k - current_node.val in sums_to_node.keys():
            counter += sums_to_node[k-current_node.val] 

        sum_dict = {}
        #update the path to dict
        for key, val in sums_to_node.items():
            sum_dict[key+current_node.val] = val



        if current_node.right:
            node_stack.append(current_node.right, sum_dict)
        if current_node.left:
            node_stack.append(current_node.left, sum_dict)
    return counter

def recdfs(node, cumsum,val_tracker,k):
    #If I do this recursively I will naturally backtrack properly so this might be easier
    if not node:
        return 0
    
    cumsum += node.val

    #If the cumsum - k is in the val_tracker we can increment the tally of vals
    path_counter = val_tracker.get(cumsum-k,0)
    
    #Update the tracker with this new path
    val_tracker[cumsum] = val_tracker.get(cumsum,0) + 1 #See how many paths we have and add 1 for the new one that we have found

    path_counter += recdfs(node.left,cumsum,val_tracker,k)
    path_counter += recdfs(node.right,cumsum,val_tracker,k)

    #Now we have exhausted all the paths from that node so we remove it
    val_tracker[cumsum] -=1

    return path_counter


