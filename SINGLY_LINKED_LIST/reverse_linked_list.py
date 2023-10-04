def reverse_linked_list(head):
  
  prev = None
  curr = head
  next = None

  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

  return prev


class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# The linked list is reversed.
reversed_head = reverse_linked_list(head)


print(reversed_head.val)
