def find_length_of_loop_in_linked_list(head):
    





class Solution:
    def detectCycle(self, head):
        # Step 1: Initialize pointers
        slow, fast = head, head
        
         # Step 2: Detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break  # Cycle detected
        
        # Step 3: Check for no cycle
        if not fast or not fast.next:
            return None  # No cycle
        
         # Step 4: Find the starting node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # Return the starting node of the cycle
        