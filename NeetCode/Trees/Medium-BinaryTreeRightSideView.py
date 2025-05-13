# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Depth-First Search Option
        if not root:
            return []

        res = []
        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
        
        #Breadth-First Search Option
        # if not root:
        #     return []
            
        # result = []
        # q = collections.deque([root])
        # while q:
        #     qLen = len(q)
        #     temp = qLen 
        #     for _ in range(qLen):
        #         node = q.popleft()
        #         temp -= 1
        #         if temp == 0:
        #             result.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return result 