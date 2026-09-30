# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0

        
        def dfs(node,value):
            if not node:
                return 
            elif node.val < value:
                dfs(node.left,value)
                dfs(node.right,value)
                return 
            # we know the node is good now
            self.count += 1
            dfs(node.left,node.val)
            dfs(node.right,node.val)
        dfs(root,float('-inf'))
        return self.count