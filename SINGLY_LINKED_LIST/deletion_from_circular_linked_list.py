class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def delete_node(head, node_to_delete):

  # If the node to be deleted is the head of the linked list.
  if node_to_delete == head:
    # Update the head pointer to point to the next node in the linked list.
    head = head.next

    # If the linked list has only one node.
    if head == node_to_delete:
      # Set the head pointer to `None`.
      head = None

  # Otherwise, the node to be deleted is not the head of the linked list.
  else:
    # Find the previous node of the node to be deleted.
    previous = head
    while previous.next != node_to_delete:
      previous = previous.next

    # Update the `next` pointer of the previous node to point to the next node in the linked list.
    previous.next = node_to_delete.next

  # Free the memory allocated to the node to be deleted.
  del node_to_delete

  return head



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head

# Delete the node with the value 2.
head = delete_node(head, Node(2))

# Print the elements of the linked list.
current = head
while current != head:
  print(current.data)
  current = current.next

# Output:
# 1
# 3
