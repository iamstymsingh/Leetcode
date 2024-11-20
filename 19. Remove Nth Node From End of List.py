# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        length = self.length(head)
        prev, cur = None, head
        k = 0
        while k < (length-n):
            prev = cur
            cur = cur.next
            k+=1

        if not prev:
            return cur.next
        else:
            prev.next = cur.next if cur.next else None
        return head

    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        return 1 + self.length(head.next)
