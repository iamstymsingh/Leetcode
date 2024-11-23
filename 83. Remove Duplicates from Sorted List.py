# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head or not head.next:
            return head

        # more than one nodes
        prev, next = head, None
        cur = head.next

        while cur:
            next = cur.next
            if cur.val == prev.val:
                prev.next = next
            else:
                prev = cur
            cur = next
        
        return head
