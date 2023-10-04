
def count_nodes_in_circular_linked_list(head):
  count = 0
  current_node = head

  while current_node is not None:
    count += 1
    current_node = current_node.next

    if current_node == head:
      break

  return count

class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head


count = count_nodes_in_circular_linked_list(head)

print("count>>", count)  # Prints 3