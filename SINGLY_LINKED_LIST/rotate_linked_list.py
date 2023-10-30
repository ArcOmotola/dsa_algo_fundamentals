def rotate_linked_list(head, k):
  if not head:
    return head
  
  # Get length
  length, tail = 1, head
  while tail.next:
    tail = tail.next
    length += 1

  k = k % length
  if k == 0:
    return head
  
  # Move to the pivot and rotate
  cur = head
  for i in range(length - k - 1):
    cur = cur.next
  newHead = cur.next
  cur.next = None
  tail.next = head

  return newHead