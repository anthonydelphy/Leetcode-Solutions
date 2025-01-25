class Solution:

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        return gcd(minNum, maxNum)