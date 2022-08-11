# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(now, mn, mx):
            if not now:
                return True
            if now.val < mn or now.val > mx:
                return False
            return True if dfs(now.left, mn, now.val-1) and dfs(now.right, now.val+1, mx) else False
        return dfs(root, -2147483648, 2147483647)