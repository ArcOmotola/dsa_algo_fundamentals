def find_loop_length(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break

  if not fast or not fast.next:
    return None
  
  count = 0
  slow = head

  while slow != fast:
    count += 1
    slow = slow.next
    fast = fast.next

  return count

# !!??






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Step 1: Initialize pointers
#         slow, fast = head, head
        
#          # Step 2: Detect if there is a cycle
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 break  # Cycle detected
        
#         # Step 3: Check for no cycle
#         if not fast or not fast.next:
#             return None  # No cycle
        
#          # Step 4: Find the starting node of the cycle
#         slow = head
#         while slow != fast:
#             slow = slow.next
#             fast = fast.next
        
#         return slow  # Return the starting node of the cycle
        