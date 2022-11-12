# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 stack.append(node.left)
#                 stack.append(node.right)
#                 res = [node.val] + res
                
#         return res

        if not root:
            return []
        
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return (left + right +[root.val])
    
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else[]
            