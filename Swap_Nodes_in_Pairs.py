
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to help with edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Swapping the nodes
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move to the next pair
            current = first
        
        # Return the new head of the list
        return dummy.next