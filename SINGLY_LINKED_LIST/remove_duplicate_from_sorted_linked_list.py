class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def remove_duplicates(head):
  current = head
  previous = None

  while current is not None:
    if current.data == previous.data:
      current = current.next
    else:
      previous = current
      current = current.next

  return previous





head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)


remove_duplicates(head)