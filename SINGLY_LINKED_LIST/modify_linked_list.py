def modify_linked_list(head, modify_function):
  # Traverse the linked list and modify the data of each node as needed.
  current = head
  while current is not None:
    current = modify_function(current)
    current = current.next
  
  # Return the head of the modified linked list.
  return head



"""The modify_function can be any function that takes a node as 
input and returns the modified node. For example, we could use the 
following modify_function to double the value of each node in the linked list:"""

def double_value(node):
  node.data *= 2
  return node



# ///////////// 

def insert_new_node(node):
  new_node = Node(node.data + 1)
  new_node.next = node.next
  node.next = new_node
  return node


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
