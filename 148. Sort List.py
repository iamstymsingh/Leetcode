# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        middle_node = self.findMiddle(head)
        head2 = middle_node.next
        middle_node.next = None

        return self.mergeTwoLists(self.sortList(head), self.sortList(head2))
    
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t,h = head, head.next
        while h and h.next:
            t,h = t.next, h.next.next
        
        return t

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        nhead = ListNode(-1)
        dummy = nhead
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            
        if list1:
            dummy.next = list1

        if list2:
            dummy.next = list2

        return nhead.next