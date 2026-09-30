# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can add the right most node at each level
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            levelS = len(q)
            for _ in range(levelS-1):
                node = q.popleft()
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right) 

            # we now just have the right most node, so pop it, append 
            # children to q, append val to root
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            res.append(node.val)
        return res
            

        