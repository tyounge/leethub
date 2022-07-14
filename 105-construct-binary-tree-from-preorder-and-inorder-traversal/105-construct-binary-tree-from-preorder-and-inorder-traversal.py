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
        pre_idx = [-1 for _ in range(6001)]
        for i, j in enumerate(inorder):
            pre_idx[j+3000] = i
        def dfs(s, e):
            global idx
            if s > e:
                return None
            m = pre_idx[preorder[idx]+3000]
            root = TreeNode(val = preorder[idx])
            idx+=1
            root.left = dfs(s, m-1)
            root.right = dfs(m+1,e)
            return root
        return dfs(0, len(preorder)-1)
            