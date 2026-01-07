class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
    
class Linked_List():
    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = Node(val)
        if self.head is None: 
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    def traverse(self):
        current = self.head 
        while current is not None: 
            print(current.val)
            current = current.next

# Code to Travese through a list and add the digits

class Solution():
    def add_linked_lists(self, list_1: Linked_List, list_2: Linked_List):
        temp = Linked_List()
        temp.head = Node(0)
        current = temp.head
        carry = 0

        l1 = list_1.head
        l2 = list_2.head

        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0 

            total = val1 + val2 + carry
            digit = total%10
            carry = total//10

            current.next = Node(digit)
            current = current.next 

            if l1 is not None: 
                l1 = l1.next 
            if l2 is not None: 
                l2 = l2.next
        
        return temp.head.next 

