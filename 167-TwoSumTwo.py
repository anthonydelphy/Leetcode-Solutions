# Time Complexity: O(n)
 # Since the given array is sorted already, 
 # #we can simply use two pointers to solve the problem in O(n). 
 # The reason that we do not sort the problem in Two Sum I is 
 # because the time complexity of sorting in the best case scenario is O(n log n). 
 # The solution that we have for Two Sum I has a time complexity of O(n), 
 # so sorting it will slow it down.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        # Create two left and right pointers
        r = len(numbers) - 1
        l = 0

        #If the sum of the pointers is too small, move the left pointer rightward. If the sum of the pointers is too large, move the right pointer leftward. Since there is a guranteed answer, we will eventually reach the correct answer.
        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]