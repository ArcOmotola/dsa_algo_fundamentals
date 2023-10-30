def delete_node(node_to_delete):
  """Deletes a node in a singly linked list, given only a pointer to that node.

  Args:
    node_to_delete: The node to be deleted.
  """
  node_to_delete.data = node_to_delete.next.data
  node_to_delete.next = node_to_delete.next.next
  