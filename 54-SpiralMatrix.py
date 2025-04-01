
# Note: It's important to Mark Spot -> Check if next is available -> if not, alter direction. If available, continue.
# Messing up this order is difficult to debug
# Setting values to None is also a great way of marking sections as visited in-place
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        x = 0
        y = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)] 
        directionIndex = 0  
  
        def valid(x, y):
            return (0 <= x < len(matrix)) and (0 <= y < len(matrix[0])) and matrix[x][y] is not None
        
        while len(result) < len(matrix) * len(matrix[0]):
            result.append(matrix[x][y])
            matrix[x][y] = None  
            
            next_x = x + directions[directionIndex][0]
            next_y = y + directions[directionIndex][1]
            
            if not valid(next_x, next_y):
                directionIndex = (directionIndex + 1) % 4
                next_x = x + directions[directionIndex][0]
                next_y = y + directions[directionIndex][1]
                
            x, y = next_x, next_y
        
        return result
