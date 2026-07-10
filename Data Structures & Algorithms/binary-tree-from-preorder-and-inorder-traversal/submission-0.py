# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # Everything to the left of rootIndex in inorder goes to left tree
        rootIndex = inorder.index(preorder[0])
        # Root index also tells how many elements are in the left tree
        root.left = self.buildTree(preorder[1:rootIndex+1],inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex+1:],inorder[rootIndex+1:])
        return root