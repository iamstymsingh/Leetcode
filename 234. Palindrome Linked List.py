# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle node
        middle = self.findMiddle(head)
        head2 = middle.next
        middle.next = None

        # reverse the second ll
        head_new = self.reverseList(head2)

        # check for palindrome
        while head and head_new:
            if head.val != head_new.val:
                return False
            if head:
                head = head.next
            if head_new:
                head_new = head_new.next
                
        return True

    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t,h = head, head.next
        while h and h.next:
            t,h = t.next, h.next.next
        
        return t
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next = None, None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev