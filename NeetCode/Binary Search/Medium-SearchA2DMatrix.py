class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        rowLeft, rowRight = 0, rows-1

        #Binary Search Rows
        while rowLeft <= rowRight:
            rowMiddle = rowLeft + (rowRight - rowLeft) // 2
            if target > matrix[rowMiddle][-1]:
                rowLeft = rowMiddle + 1
            elif target < matrix[rowMiddle][0]:
                rowRight = rowMiddle -1
            else:
                break
          
        # No Correct Row Range
        if not (rowLeft <= rowRight):
            return False
        
        #Binary Search Columns
        rowMiddle = rowLeft + (rowRight - rowLeft) // 2
        l, r = 0, cols-1
        while l <= r:
            m = l + ((r-l)//2) 
            if target > matrix[rowMiddle][m]:
                l = m+1
            elif target < matrix[rowMiddle][m]:
                r = m-1
            else:
                return True
        return False


        # Original Solution O(m * Log(n))
        # for i in range(len(matrix)):
        #     if (i == len(matrix)-1) or (matrix[i][0] <= target and target < matrix[i+1][0]):
        #         col = i
        #         l, r = 0, len(matrix[col])-1
                
        #         while l <= r:
        #             m = l + ((r-l)//2)

        #             if target < matrix[i][m]:
        #                 r = m-1
        #             elif target > matrix[i][m]:
        #                 l = m+1
        #             else:
        #                 return True
        
        # return False
            

            