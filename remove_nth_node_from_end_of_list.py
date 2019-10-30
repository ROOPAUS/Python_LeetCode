
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

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
        

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
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
print("head is", a_llist.head)
n1 = int(input('which node would you like to remove? '))
a_llist.removeNthFromEnd(a_llist.head,n1)
a_llist.display()
        
            
    
    
 
