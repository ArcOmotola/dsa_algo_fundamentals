def delete_node(node_to_delete):
  node_to_delete.data = node_to_delete.next.data
  node_to_delete.next = node_to_delete.next.next
  