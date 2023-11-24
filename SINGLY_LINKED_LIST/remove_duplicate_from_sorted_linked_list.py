# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None


# def remove_duplicates(head):
#   current = head
#   previous = None

#   while current is not None:
#     if current.data == previous.data:
#       current = current.next
#     else:
#       previous = current
#       current = current.next

#   return previous



# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None


# head = Node(1)
# head.next = Node(1)
# head.next.next = Node(2)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(3)


# remove_duplicates(head)



def remove_duplicates(head):
  cur = head

  while cur:
    while cur.next and cur.next.val == cur.val:
      cur.next = cur.next.next
    cur = cur.next
  return head



class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)


remove_duplicates(head)





# class ListNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.next = None

# def deleteDuplicates(head):
#     current = head
    
#     while current and current.next:
#         if current.val == current.next.val:
#             current.next = current.next.next
#         else:
#             current = current.next
            
#     return head
