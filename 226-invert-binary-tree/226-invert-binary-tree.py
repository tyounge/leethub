# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(now):
            if not now:
                return
            dfs(now.left)
            dfs(now.right)
            now.left, now.right = now.right, now.left
        
        dfs(root)
        return root
        