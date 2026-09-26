# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if we dont have a root, return true
        # else, if the height of the left and right trees differ by more than 1, return false
        if not root:
            return True
        
        def height(tree):
            if not tree:
                return 0
            return 1 + max(height(tree.left),height(tree.right))
        if abs(height(root.left)-height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        