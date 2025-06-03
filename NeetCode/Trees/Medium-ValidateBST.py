# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerBound, upperBound):
            if not root:
                return True
            result = False
            if lowerBound < root.val < upperBound:
                result = True

            return result and (dfs(root.left, lowerBound, root.val)) and (dfs(root.right, root.val, upperBound))
        return dfs(root, float("-inf"), float("inf"))