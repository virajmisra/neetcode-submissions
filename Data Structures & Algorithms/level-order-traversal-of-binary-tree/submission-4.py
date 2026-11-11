# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = collections.deque()
        res = []
        nodes.append(root)
        while nodes:
            levelSize = len(nodes)
            level = []
            for _ in range(levelSize):
                n = nodes.popleft()
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)
                level.append(n.val)
            res.append(level)
        return res
        
