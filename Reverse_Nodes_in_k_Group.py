# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a portion of the list
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointers initialization
        group_prev = dummy
        
        while True:
            # Find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # If there are fewer than k nodes left, return the result
            
            group_next = kth.next
            
            # Reverse the group
            prev, curr = group_prev.next, group_prev.next.next
            for _ in range(k - 1):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Adjust pointers
            start = group_prev.next
            start.next = group_next
            group_prev.next = prev
            
            # Move to the next group
            group_prev = start