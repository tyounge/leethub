# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        global idx
        idx = 0
        pre_idx = {j : i for i,j in enumerate(inorder)}
        def dfs(s, e):
            global idx
            if s > e:
                return None
            val = preorder[idx]
            idx+=1
            m = pre_idx[val]
            root = TreeNode(val, dfs(s,m-1), dfs(m+1,e))
            return root
        return dfs(0, len(preorder)-1)
            