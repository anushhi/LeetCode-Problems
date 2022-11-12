# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]
        while q:
            node = q.pop()
            if node:
                q.append(node.left)
                q.append(node.right)
                res = [node.val] + res
                
        return res

#         if not root:
#             return []
        
#         left = self.postorderTraversal(root.left)
#         right = self.postorderTraversal(root.right)
#         return (left + right +[root.val])
    
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else[]
            