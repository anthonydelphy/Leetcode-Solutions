class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0
        l,r = 0, len(heights)-1
        while l < r:
            minHeight = min(heights[l],heights[r])
            area = (r-l) * minHeight
            if maxAr < area:
                maxAr = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return maxAr
        
        #First solution: O(n^2)
        # maxAr = 0
        # result = -1
        # for i in range(len(heights)):
        #     for x in range(len(heights)-1, i,-1):
        #         minHeight = min(heights[i],heights[x])
        #         area = (x-i) * minHeight
        #         if maxAr < (area):
        #             maxAr = area
        # return maxAr
