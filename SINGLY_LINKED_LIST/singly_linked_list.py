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



