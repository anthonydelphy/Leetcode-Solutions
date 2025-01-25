# Time Complexity: O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = [1] * len(ratings)

        # Going rightward, check the index against it's leftward neighbor and add candy as needed
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                result[i] = result[i-1] + 1
        
        # Going leftward, check the index against it's rightward neighbor and add candy as needed
        # Since values have already been populated, you must also check the edgecase in which
        # more candy have been added to the cursor location than its rightward neighbor
        for i in range (len(ratings) -2, -1, -1):
            if ratings[i] > ratings[i+1]:
                #Edge case in which the cursors rightward neighbor candy is smaller.
                result[i] = max(result[i], result[i+1] +1)
        
        return sum(result)
