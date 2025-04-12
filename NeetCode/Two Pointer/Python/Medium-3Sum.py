class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)

        for x in range(len(nums)):
            k = nums[x]
            l,r = x+1, len(nums)-1
            while l < r:
                eq = nums[l] + nums[r] + k
                if eq == 0:
                    result.append([nums[l],nums[r],k])
                elif eq < 0:
                    l+=1
                else:
                    r-=1



        return result