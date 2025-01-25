class Solution:

    
    """ If you want to do this recursively,
    def gcd(a,b):
        if(b == 0):
            return a
        else:
            return gcd(b,a % b) """
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        return gcd(minNum, maxNum)