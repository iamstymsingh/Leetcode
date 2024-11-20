# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        nhead = ListNode(-1)
        dummy = nhead

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            summed_val = v1+v2+carry
            dummy.next = ListNode(summed_val % 10)
            carry = summed_val // 10 if summed_val > 9 else 0
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return nhead.next