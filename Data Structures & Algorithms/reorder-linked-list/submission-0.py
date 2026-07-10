# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle 
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # break into halves
        secondHalf = slow.next
        slow.next = None
        # Rev second half
        prev = None
        while secondHalf:
            n = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = n

        firstHalf = head
        secondHalf = prev

        # halves are either equal in size of second is 1 shorter
        # so we can just keep going until second is null
        while secondHalf:
            t1 = firstHalf.next
            t2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = t1
            firstHalf = t1
            secondHalf = t2
