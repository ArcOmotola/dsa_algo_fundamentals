class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    #INSERT AT THE BEGINNING
    #To insert a node at the beginning, we need to adjust the next pointer of the new node to point to the current head of the list.
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    #INSERT AT THE END
    #To insert a node at the end, we need to traverse the list until we reach the last node, and then update the next pointer of the last node to point to the new node.
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:   #for empty linked list case (The head pointer doesn’t point to anything at all, and therefore there is no node in the linked list)
            self.head = new_node
            return
        
        last_node = self.head   #for non-empty linked list case ( It will start at the beginning of the linked list and move through the linked list as long as the last_node.next doesn’t point to None. We keep moving from node to node until we get to the last_node where last_node.next will point to None and will terminate the while loop. After the while loop concludes, last_node points to the last node.)
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    #INSERT AT A SPECIFIC POSITION
    # To insert a node at a specific position, we need to find the node at that position and adjust the next pointers accordingly.
    
    # def insert_at_position(self, data, position):
    #     if position == 0:
    #         self.insert_at_beginning(data)
    #         return
    #     new_node = Node(data)
    #     current_node = self.head
    #     for _ in range(position - 1):
    #         if current_node is None:
    #             raise IndexError("Invalid position")
    #         current_node = current_node.next
    #     new_node.next = current_node.next
    #     current_node.next = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:                           #check if the node to be inserted after is in the linked list or not
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next         # set the next pointer of the new node to point to what the next pointer of the prev_node is
        prev_node.next = new_node              # change the next pointer of the prev_node to point to the new node
        

    def delete_node_position(self, position):
        if self.head is None:
          return
        if position == 0:
          self.head = self.head.next
          return
        
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None or current_node.next is None:
                raise IndexError("Invalid position")
            current_node = current_node.next
            current_node.next = current_node.next.next
        
        
    def delete_node_position(self, position):
        cure_node = self.head
    


    def print_list(self):
        cur_node = self.head
        while cur_node:          # Then we use a while loop which keeps running and printing the data if cur_node is not equal to None.
            print(cur_node.data)
            cur_node = cur_node.next
    

llist = SinglyLinkedList()

llist.insert_at_end("A")
llist.insert_at_end("B")
llist.insert_at_end("C")
llist.insert_at_end("D")
# llist.insert_at_beginning("E")
llist.insert_after_node(llist.head.next, "D")

llist.print_list() 








# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class MyLinkedList:

#     def __init__(self):
#         self.head = None  # Initialize an empty linked list
#         self.size = 0

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1  # Index is invalid
#         curr = self.head
#         for _ in range(index):
#             curr = curr.next
#         return curr.val

#     def addAtHead(self, val: int) -> None:
#         new_node = ListNode(val, self.head)
#         self.head = new_node
#         self.size += 1

#     def addAtTail(self, val: int) -> None:
#         new_node = ListNode(val)
#         if not self.head:
#             self.head = new_node
#         else:
#             curr = self.head
#             while curr.next:
#                 curr = curr.next
#             curr.next = new_node
#         self.size += 1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return  # Index is out of bounds
#         if index == 0:
#             self.addAtHead(val)
#         else:
#             new_node = ListNode(val)
#             curr = self.head
#             for _ in range(index - 1):
#                 curr = curr.next
#             new_node.next = curr.next
#             curr.next = new_node
#             self.size += 1

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return  # Index is invalid
#         if index == 0:
#             self.head = self.head.next
#         else:
#             curr = self.head
#             for _ in range(index - 1):
#                 curr = curr.next
#             curr.next = curr.next.next
#         self.size -= 1









# class Node:
#   def __init__(self, val):
#     self.val = val
#     self._next = None

#   def get_next(self):
#     return self._next

#   def set_next(self, node):
#     self._next = node

# class LinkedList:
#   def __init__(self):
#     self._head = None

#   def add_at_head(self, val):
#     new_node = Node(val)
#     new_node.set_next(self._head)
#     self._head = new_node

#   def get_head(self):
#     return self._head

#   def traverse(self):
#     current_node = self._head
#     while current_node is not None:
#       print(current_node.val)
#       current_node = current_node.get_next()

# # Example usage:

# linked_list = LinkedList()

# linked_list.add_at_head(1)
# linked_list.add_at_head(2)
# linked_list.add_at_head(3)

# linked_list.traverse()
