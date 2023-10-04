def exchange_first_and_last_nodes_in_circular_linked_list(head):
  current_node = head

  while current_node.next != head:
    current_node = current_node.next
  
  current_node, head = head, current_node

  return head 


class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head

# The first and last nodes of the circular linked list are exchanged.
head = exchange_first_and_last_nodes_in_circular_linked_list(head)

print("ansss>>>", head.val)
# The circular linked list can now be traversed by starting at the head and
# following the next pointers until you reach the head again.
