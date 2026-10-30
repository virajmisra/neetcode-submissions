# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # a path can be diameter, so we can look at the same approach of diameter but keeping track of a sum
        # dfs function to return the sum of a path
        
        self.res = root.val
        def dfs(node, total):
            if not node:
                return total
            l = max(dfs(node.left, total),0)
            r = max(dfs(node.right, total),0)
            self.res = max(self.res, l + r + node.val)
            return node.val + max(l,r)
        dfs(root,0)
        return self.res
        
