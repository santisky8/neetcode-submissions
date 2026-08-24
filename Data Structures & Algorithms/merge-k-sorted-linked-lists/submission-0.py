import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        hq = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(hq, (l.val, i, l))

        while hq:
            val, i, node = heapq.heappop(hq)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(hq, (node.next.val, i, node.next))

        return dummy.next