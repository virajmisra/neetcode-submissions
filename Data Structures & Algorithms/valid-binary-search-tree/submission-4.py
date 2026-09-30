# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node,sm,la):
            if not node:
                return True
            if node.val <= sm or node.val >= la:
                return False
            return validate(node.right,node.val,la) and validate(node.left,sm,node.val)
        return validate(root,float('-inf'),float('inf'))