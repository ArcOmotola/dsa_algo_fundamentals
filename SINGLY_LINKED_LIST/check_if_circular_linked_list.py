class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

def is_circular_linked_list(head):
  slow, fast = head, head

  while fast and fast.next:
    if slow == fast:
      return True
    slow = slow.next
    fast = fast.next.next

  return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head

is_circular = is_circular_linked_list(head)

print("is it circular??", is_circular)  # Prints True



