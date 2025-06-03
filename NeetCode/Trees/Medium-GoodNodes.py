# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root,mx):
            nonlocal res
            if not root:
                return 0
            
            res += 1 if root.val >= mx else 0
            tempMax = max(mx, root.val) 
            dfs(root.left, tempMax)
            dfs(root.right, tempMax)
        
        dfs(root,root.val)
        return res
