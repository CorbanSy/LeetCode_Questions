# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Compute the length of the list and get the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Connect the tail to the head to make it circular
        tail.next = head

        # Calculate the new tail position (length - k % length - 1) and new head position (length - k % length)
        k = k % length
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head