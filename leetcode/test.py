# # # 19. Remove Nth Node From End of List
# # # Medium Topics premium lock iconCompanies

# # # Given the head of a linked list, remove the nth node from the end of the list and return its head.
# # # Example 1:
# # # Input: head = [1,2,3,4,5], n = 2
# # # Output: [1,2,3,5]
# # # Example 2:
# # # Input: head = [1], n = 1
# # # Output: []
# # # Example 3:
# # # Input: head = [1,2], n = 1
# # # Output: [1]
# # # Constraints:
# # #     The number of nodes in the list is sz.
# # #     1 <= sz <= 30
# # #     0 <= Node.val <= 100
# # #     1 <= n <= sz
# # # Follow up: Could you do this in one pass?
 
# # class Single_Node:
# #     def __init__(self, val = 0, next = None):
# #         self.val = val
# #         self.next = next 

# # class Single_Linked_List:
# #     def __init__(self, val= None):
# #         self.head = None
# #         if val is not None:
# #             self.head = self._to_node(val)

# #     def _to_node(self, val):
# #         if isinstance(val, Single_Node):
# #             return val 
# #         return Single_Node(val)  

# #     def add(self, val):
# #         new_Node = self._to_node(val)

# #         if self.head is None:
# #             self.head = new_Node
# #             return 
        
# #         current = self.head
# #         while current.next is not None:
# #             current = current.next
# #         current.next = new_Node
    
# #     def delete_Node(self, index):
# #         if self.head is None:
# #             print("List is empty")
# #             return 

# #         if index == 1:
# #             self.head = self.head.next
# #             return 

# #         count = 1
# #         current = self.head 
        
# #         while current.next is not None:
# #             if count == index - 1:
# #                 current.next = current.next.next 
# #                 return 
# #             current = current.next
# #             count += 1 

# #         print(f"There is no Node with that index.")
    
# #     def show_all(self):
# #         current = self.head 

# #         while current is not None:
# #             print(f"{current.val} --> ", end = "")
# #             current = current.next
# #         print("None")

# # First_Node = Single_Node(10)
# # Second_Node = Single_Node(20)
# # Third_Node = Single_Node(30)
# # Fourth_Node = Single_Node(40)
# # Fifth_Node = Single_Node(50)

# # my_linked_list = Single_Linked_List()
# # my_linked_list.add(First_Node)
# # my_linked_list.add(Second_Node)
# # my_linked_list.add(Third_Node)
# # my_linked_list.add(Fourth_Node)
# # my_linked_list.add(Fifth_Node)

# # my_linked_list.show_all()
# # my_linked_list.delete_Node(2)
# # my_linked_list.show_all()

# # Remove Nth Node From End of linked_list

# class Single_Node:
#     def __init__(self, val = 0, next = None):
#         self.val = val 
#         self.next = next 

# class Single_Linked_List: 
#     def __init__(self, item = None):
#         self.head = None

#         if item is not None: 
#             new_Node = self.to_Node(item)
#             self.head = new_Node

#     def to_Node(self, item): 
#         if isinstance(item, Single_Node):
#             return item 
#         return Single_Node(item)

#     def add_to_end(self, item):
#         new_Node = self.to_Node(item)

#         if self.head is None: 
#             self.head = new_Node
        
#         current = self.head 
#         while current.next is not None: 
#             current = current.next 
#         current.next = new_Node

#     def add_to_front(self, item):
#         new_Node = self.to_Node(item)
#         new_Node.next = self.head 
#         self.head = new_Node
    
#     def add_at_index(self, item = None, index = None):
#         if index == None: 
#             print("Forgot to provide index")
#             return 

#         if self.head is None:
#             print("List is empty")
#             return 
        
#         if item == None: 
#             print("Forgot to provide Node")
#             return 

#         if index == 0:
#             self.add_to_front(item)
#             return 
        
#         new_Node = self.to_Node(item)
        
#         current = self.head 
#         count = 0  
#         while current.next is not None: 
#             if count == index - 1:
#                 new_Node.next = current.next 
#                 current.next = new_Node
#                 return 
#             count += 1
#             current = current.next
    
#     def del_from_index(self, index= None):
#         if index == None: 
#             print("Forgot to provide index")
#             return 

#         if self.head is None:
#             print("List is empty")
#             return 
        
#         if index == 0:
#             self.head = self.head.next 

#         count = 0 
#         current = self.head 
#         while current.next is not None: 
#             if count == index - 1:
#                 current.next = current.next.next 
#                 return 
#             count += 1 
#             current = current.next 
    
#     def del_from_end_of_list(self, index = None):
#         if index == None: 
#             print("Forgot to provide index")
#             return 
        
#         if self.head is None:
#             print("List is empty")
#             return 
        
#         count = 0
#         current = self.head 
#         while current is not None: 
#             current = current.next
#             count += 1 
        
#         index_to_kill = count - index 
#         if index_to_kill == 0:
#             self.head = self.head.next 

#         count = 0 
#         current = self.head 
#         while current is not None: 
#             if count == index_to_kill - 1:
#                 current.next = current.next.next
#             current = current.next 
#             count += 1
# for i in range(10,0,-1):
#     print(i)

# print(int(6/-132))
# print(int(13/5))

# word1 = "abc"
# word2 = "def"

# index = 0
# final_string = [] 
# while index < len(word1) or index < len(word2):
#     try: 

#     if IndexError continue else final_string.append(word1[index])
#     final_string.append(word2[index]) if not IndexError else final_string.append(word2[index])
#     index += 1


# print(final_string)

# print(1 // 2 * 3)
# blocks = int(input("Enter the number of blocks: "))

# current_layer = 0 
# current_layer_blocks = 0
# layer_blocks = 1 
# height = 0

# for i in range(1, blocks):
#     current_layer_blocks += 1 
#     if current_layer_blocks == layer_blocks:
#         height += 1 
#         layer_blocks += 1 
#         current_layer_blocks = 0 
        
# print("The height of the pyramid:", height)

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
 
# del list_1[0]
# del list_2
 
# print(list_3)


# var = 1 
# while var < 10:
#     print("1")
#     var = var << 1

# list_1 = [i for i in range(-1,2)]
# print(list_1)