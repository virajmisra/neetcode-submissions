# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # go as left as possible
        # when there is no left, pop everything in q
        # everytime you pop up, k -= 1
        # when k == 0, return curr
        nodes = []
        nodes.append(root)
        curr = root
        while True:
            while curr:
                nodes.append(curr)
                curr = curr.left
            # Ensures we are at leftmost node every time,
            # so everytime we can decrement k until 0 since we see
            # smallest, 2nd smallest, etc.
            curr = nodes.pop()
            k -= 1
            if 0 == k:
                return curr.val
            curr = curr.right
        return -1