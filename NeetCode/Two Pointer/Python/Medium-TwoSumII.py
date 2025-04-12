class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0 , len(numbers)-1
        while l < r:
            tSum = numbers[l] + numbers[r]
            if tSum == target:
                return [l+1,r+1]
            elif tSum > target:
                r -= 1
            elif tSum < target:
                l +=1
        return -1