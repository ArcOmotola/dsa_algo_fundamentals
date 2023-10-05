def traverse_circular_linked_list(head):
  """Traverses a circular linked list.

  Args:
    head: The head of the circular linked list.
  """

  current_node = head

  while current_node != head:
    print(current_node.val)
    current_node = current_node.next

  print("222>>",current_node.val)



class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head

# The circular linked list is traversed and the data of each node is printed.
traverse_circular_linked_list(head)
