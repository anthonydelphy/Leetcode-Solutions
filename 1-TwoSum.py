class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}

        #Key value pair is index, value
        for i, x in enumerate(nums):
            difference = target - x
            if difference in diction:
                return (i, diction[difference])
            diction[x] = i


# This is the solution I typically think of first.
# # Two-Loop solution. Time complexity of O(n).

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         diction = {}
        
#         # Create dictionary
#         # the key will be the value of the array while the actual value stored is the index where the value is found.
#         for i, x in enumerate(nums):
#             diction[x] = i

#         for i, x in enumerate(nums):
#         # Find the value that is required to get to the target and see if it exists in the dictionary. 
#             complement = target - nums[i]
#             #ensure that we are NOT looking at the same number we are currently iterating on. The answer must be different indexes
#             if complement in diction and diction[complement] != i:
#                 return [i, diction[complement]]
