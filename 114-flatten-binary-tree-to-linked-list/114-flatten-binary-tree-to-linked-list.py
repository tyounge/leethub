# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node):
        if node == None:
            return None
        if node.left == node.right == None:
            return node
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        print(node,l,r)
        if l:
            l.right = node.right
            node.right = node.left
        node.left = None
        print(node,l,r)
        
        return r if r else l
            
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.dfs(root)
        return root
        