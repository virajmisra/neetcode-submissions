# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        curr = root
        nodes.append(curr)
        count = 0
        while nodes:
            while curr:
                nodes.append(curr)
                curr = curr.left
            node = nodes.pop()
            count+=1
            if count==k:
                return node.val
            curr = node.right
        return -1
        