def rotate_doubly_linked_list(head, n):
  current = head

  for i in range(n):
    current = current.next

  new_head = current

  