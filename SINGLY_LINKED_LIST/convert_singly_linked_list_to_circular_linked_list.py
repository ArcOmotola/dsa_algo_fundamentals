def convert_singly_linked_list_to_circular_linked_list(head):
  current_node = head

  while current_node.next is not None:
    current_node = current_node.next
  current_node.next = head
  return head


class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head = convert_singly_linked_list_to_circular_linked_list(head)

print(head.next.next.next.val)