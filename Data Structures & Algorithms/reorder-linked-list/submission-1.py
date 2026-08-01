# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            n = second.next
            second.next = prev
            prev = second
            second = n
        
        while prev:
            t1 = head.next
            t2 = prev.next

            head.next = prev
            prev.next = t1

            head = t1
            prev = t2




