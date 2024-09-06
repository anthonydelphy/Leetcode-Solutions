class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #Sorting is necessary to allow for the problem to devolve into two sum 2
        nums.sort()

        for i,a in enumerate(nums):

            # If we are solving the problem, we do not want duplicates in the response. a == num[i-1] ensures that if a value is the same as the number prior to it, we do not need to check it, as it has already been checked in a previous loop
            if i > 0 and a == nums[i - 1]:
                continue

            l = i+1
            r = len(nums) -1
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a , nums[l] , nums[r]])
                    l+=1
                    # Do what was done above again since there WAS a solution and we don't want duplicate solutions, so move upward until we are either at a brand new number of we are done check (l < r)
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res