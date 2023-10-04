class ListNode:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

def findMiddle(head):
  if not head:
    return None
  
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

#create a sample linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
# Find the middle node
middle_node = findMiddle(node1)

print("Middle guy>>>", middle_node.val)