def removeElements(head, val): 
  dummy = ListNode(next=head)
  prev, curr = dummy, head


  while curr:
    nxt = curr.next

    