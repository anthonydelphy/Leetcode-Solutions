# Time Complexity: O(n^2)
# The daily problem for tomorrow, (04/03) will likely have
# heavier constraints and require a better solution
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        left = nums[0]

        for b in range(1 , len(nums)):  # b starts at a+1 to prevent repetition
            if nums[b] > left:
                left = nums[b]
                continue

            for c in range(b + 1, len(nums)):
                result = max(result, (left - nums[b]) * nums[c])
                        
        return result
        