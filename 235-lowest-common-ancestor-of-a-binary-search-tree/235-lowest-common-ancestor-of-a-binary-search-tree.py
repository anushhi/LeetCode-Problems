# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if node is None:
            return None
        if p.val < node.val and q.val < node.val:
            return self.lowestCommonAncestor(node.left,p,q)
        elif p.val > node.val and q.val > node.val:
            return self.lowestCommonAncestor(node.right,p,q)
        else:
            return node