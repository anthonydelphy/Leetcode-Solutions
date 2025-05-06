# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Key = [Balanced Bool, Depth]
        def dfs(root, height):
            if not root:
                return [True, 0]

            left = dfs(root.left, height+1)
            right = dfs(root.right, height+1)
            
            balanced = abs(left[1]-right[1]) <= 1 and left[0] and right[0]
            
            return [abs(left[1]-right[1]) <= 1 and left[0] and right[0], 1 + max(left[1], right[1])]
        
        return dfs(root,0)[0]
        