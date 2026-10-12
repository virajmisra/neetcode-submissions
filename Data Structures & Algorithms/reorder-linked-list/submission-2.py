# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        curr = None

        while second:
            n = second.next
            second.next = curr
            curr = second
            second = n
        
        while curr:
            t1 = curr.next
            t2 = head.next

            head.next = curr
            curr.next = t2

            curr = t1
            head = t2
        
        