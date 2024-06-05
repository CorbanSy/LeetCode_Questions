# Definition for singly-linked list.
from heapq import heappush, heappop
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a heap
        min_heap = []
        
        # Insert the first node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))
        
        # Dummy head for the resulting merged list
        dummy = ListNode()
        current = dummy
        
        # Extract the smallest node from the heap and push its next node to the heap
        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next