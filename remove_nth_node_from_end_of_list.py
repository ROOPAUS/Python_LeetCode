# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#the commented code takes 2 traversals, 1 for finding length and other for removing nth node
#the second code takes only 1 traversal
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        num_nodes=0
        while(temp is not None):
            temp=temp.next
            num_nodes+=1
        k = num_nodes-n
        
        prev=None
        ptr=head
        while(k!=0):
            prev=ptr
            ptr=ptr.next
            k-=1
        if(prev is None):
            return head.next
        else:
            prev.next=ptr.next
            ptr.next=None
            return head
 '''           

class Solution:
    def removeNthFromEnd(self, head, n):
        if (head is None):
            return None
        prev = ptr = head
        for i in range(n):
            ptr = ptr.next
        if (ptr is None):
            head = head.next
            return head
        while (ptr.next is not None):
            ptr = ptr.next
            prev = prev.next
        curr = prev.next
        prev.next = curr.next
        return head
        
            
    
    
 
