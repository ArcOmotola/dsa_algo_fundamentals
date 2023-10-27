
# ?????????? POSSIBLY WRONG


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def find_middle_node(head):
  if not head:
    return None
  
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

def split_circular_linked_list(head):
  middle_node = find_middle_node(head)

  middle_node.next = None

  return head, middle_node.next




head = Node(3)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = head

head1, head2 = split_circular_linked_list(head)

# Print the two halves of the circular linked list.
while head1 is not None:
  print(head1.data)
  head1 = head1.next

while head2 is not None:
  print(head2.data)
  head2 = head2.next

# Output:
# 3
# 2
# 1
