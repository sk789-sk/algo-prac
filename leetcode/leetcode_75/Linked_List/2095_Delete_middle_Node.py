# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#find middle -1 node and have it point to middle +1 node is the goal 
#We could do this by first finding the end then calculating the middle and then subtracting 1.
#We will pass over this node tho so maybe we can manipulate it so that when we reach the end of the string we have another pointer at this node. 
#The fast and slow pointer method will have midpoint and end if they both start at 0. #If we shift the placement of the fast pointer we could probably acheive this. if we start the fast at +2 from the slow one, it would hit the end the when the slow is at the mid-1 idx. 

def deleteMiddle(head):
    #handle lists of length 1 aka there is no head.next or head.next.next

    if not head.next:
        return []

    slow = head
    fast = head.next.next

    while fast and fast.next: #handles even and odd length lists.
        slow = head.next
        fast = fast.next.next

    slow.next = slow.next.next
    return head
    

def deleteMiddle2pass(head):
    #first lets find the middle nodes idx
    init = head
    start = head
    c = 0 
    while head:
        print(head.val)
        head = head.next
        c+=1   
    midpoint_sub1 = c//2 -1 
    while midpoint_sub1 > 0:
        start = start.next
        midpoint_sub1 -=1
    print(start.val)

    start.next = start.next.next
    return init

def createList(arr):
    
    init = ListNode(arr[0])
    start = init

    for val in arr[1:]:
        new_node = ListNode(val)
        init.next = new_node
        init=new_node

    return start

test = [1,3,4,7,1,2,6]

start_node = createList(test)

deleteMiddle(start_node)