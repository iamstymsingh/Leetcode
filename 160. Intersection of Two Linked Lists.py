# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA,lengthB = self.length(headA), self.length(headB)

        if lengthA > lengthB:
            for _ in range(lengthA - lengthB):
                headA = headA.next
        else:
            for _ in range(lengthB - lengthA):
                headB = headB.next
        
        # check for the intresection point
        while headA and headB:
            if headA == headB:
                return headA
            if headA:
                headA = headA.next
            if headB:
                headB = headB.next
        
        return None

    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        return 1 + self.length(head.next)
