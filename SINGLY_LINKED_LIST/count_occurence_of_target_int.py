
""" Write a function that counts the number
    of times a given int occurs in a Linked List
 """
class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

def count_occurrence(head, target):
  count = 0

  current_head = head
  while current_head is not None:
    if current_head.val == target:
      count += 1
    current_head = current_head.next
  return count


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)

target = 2

count = count_occurrence(head, target)

print("node count>>", count)  
