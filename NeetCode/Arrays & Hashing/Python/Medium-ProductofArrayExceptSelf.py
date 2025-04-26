class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]
        return result
    
#Time Complexity wise, this is fine. We could improve space complexity by having it be done in a single result array
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = [1] * len(nums)
#         postfix = [1] * len(nums)

#         #Calculate prefix array
#         for i in range(len(nums)):
#             if i == 0:
#                 prefix[i] = nums[i]
#             prefix[i] = prefix[i-1] * nums[i] 

#         #Calculate postfix array
#         for i in range(len(nums)-1,-1,-1):
#             if i == len(nums)-1:
#                 postfix[i] =nums[i]
#                 continue
#             postfix[i] = postfix[i+1] * nums[i] 

#         #Calculate result array
#         result = [1] * (len(nums))
#         for i in range(len(result)):
#             if i == 0:
#                 result[i] = postfix[i+1]
#                 continue
#             elif i == len(result)-1:
#                 result[i] = prefix[i-1]
#                 continue
#             result[i] = postfix[i+1] * prefix[i-1]
                
#         return result
