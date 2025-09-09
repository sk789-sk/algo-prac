# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def solution(head):
    prev = None
    current = head
    next_node = None

    if not head or not head.next:
        return head
    
    while current is not None:
        #save the next node since this link gets severed when updating
        next_node = current.next

        #update the link (reversal)
        current.next = prev

        #Save node that we will have to point to 
        prev = current


        #move along the list
        current = next_node

    #when current is none we have gone past the end of the list so previous is the head current is null, next_node would be null?. Could just end when next node is null?


    return prev

def printlist(head):
    while head:
        print(head.val)
        head = head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

test = solution(head)

printlist(test)
