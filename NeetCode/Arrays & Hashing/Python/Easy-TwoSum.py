class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in dict:
                return [dict[key], i]
            dict[nums[i]] = i
        return [-1]