# # 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

#If we Know the length of the array we can keep a record of the 1/2 values and then start adding on the second half and do this in 1 pass.
#We dont know the full length and instead just the head so we would need to traverse down the whole list to figure out the middle point.
#

#1. Traverse the List and get the total length (n).
#2. Go to index n/2
#3. Reverse the list from index n/2 to n and return node at n.
#4. Loop for i to n/2 and sum the vales at node 0 and n. 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    n = 0

    slow,fast = head, head

    while fast and fast.next: #cant overrun
        slow = slow.next
        fast = fast.next.next
    

    #reverse from mid node

    prev = None
    current = slow

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    reverse_head = prev

    max = 0

    start = head
    end = reverse_head

    while end:
        sum = start.val + end.val
        if sum > max:
            max = sum
        start = start.next
        end = end.next

    print(max)
    return max

head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(5)

solution(head)
